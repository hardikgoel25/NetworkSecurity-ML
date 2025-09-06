import re
import socket
import ssl
import whois
import requests
import pandas as pd
from urllib.parse import urlparse
from datetime import datetime
from bs4 import BeautifulSoup


def extract_features(url: str) -> pd.DataFrame:
    features = {}
    parsed = urlparse(url)
    domain = parsed.netloc

    # --- 1. having_IP_Address ---
    features["having_IP_Address"] = 1 if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain) else -1

    # --- 2. URL_Length ---
    features["URL_Length"] = len(url)

    # --- 3. Shortining_Service ---
    shorteners = r"bit\.ly|goo\.gl|tinyurl|ow\.ly|t\.co|is\.gd|buff\.ly"
    features["Shortining_Service"] = 1 if re.search(shorteners, url) else -1

    # --- 4. having_At_Symbol ---
    features["having_At_Symbol"] = 1 if "@" in url else -1

    # --- 5. double_slash_redirecting ---
    features["double_slash_redirecting"] = 1 if url.find("//", 8) != -1 else -1

    # --- 6. Prefix_Suffix ---
    features["Prefix_Suffix"] = 1 if "-" in domain else -1

    # --- 7. having_Sub_Domain ---
    features["having_Sub_Domain"] = 1 if domain.count(".") > 2 else -1

    # --- 8. SSLfinal_State ---
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3.0)
            s.connect((domain, 443))
            cert = s.getpeercert()
            if cert:
                features["SSLfinal_State"] = 1
            else:
                features["SSLfinal_State"] = -1
    except Exception:
        features["SSLfinal_State"] = -1

    # --- 9. Domain_registeration_length ---
    try:
        w = whois.whois(domain)
        exp = w.expiration_date
        if isinstance(exp, list): exp = exp[0]
        if exp:
            delta = (exp - datetime.now()).days
            features["Domain_registeration_length"] = 1 if delta > 365 else -1
        else:
            features["Domain_registeration_length"] = -1
    except:
        features["Domain_registeration_length"] = -1

    # --- 10. Favicon ---
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        icon = soup.find("link", rel=lambda x: x and "icon" in x.lower())
        if icon and domain in icon.get("href", ""):
            features["Favicon"] = 1
        else:
            features["Favicon"] = -1
    except:
        features["Favicon"] = -1

    # --- 11. port ---
    try:
        socket.create_connection((domain, 80), timeout=3)
        features["port"] = -1  # normal
    except:
        features["port"] = 1   # suspicious
    # (You can add non-standard port checks here)

    # --- 12. HTTPS_token ---
    features["HTTPS_token"] = 1 if "https" in domain else -1

    # --- 13–17. Request_URL, URL_of_Anchor, Links_in_tags, SFH, Submitting_to_email ---
    try:
        soup = BeautifulSoup(requests.get(url, timeout=5).text, "html.parser")
        # % external request URLs
        imgs = soup.find_all("img", src=True)
        features["Request_URL"] = -1 if not imgs else (1 if sum(domain not in i["src"] for i in imgs)/len(imgs) > 0.6 else -1)

        anchors = soup.find_all("a", href=True)
        features["URL_of_Anchor"] = 1 if anchors and sum(domain not in a["href"] for a in anchors)/len(anchors) > 0.6 else -1

        metas = soup.find_all("meta")
        features["Links_in_tags"] = 1 if len(metas) > 20 else -1

        forms = soup.find_all("form", action=True)
        features["SFH"] = 1 if any(f["action"] in ["", "about:blank"] for f in forms) else -1

        features["Submitting_to_email"] = 1 if "mailto:" in str(soup) else -1
    except:
        features["Request_URL"] = features["URL_of_Anchor"] = features["Links_in_tags"] = features["SFH"] = features["Submitting_to_email"] = -1

    # --- 18. Abnormal_URL ---
    features["Abnormal_URL"] = -1 if domain in url else 1

    # --- 19. Redirect ---
    try:
        r = requests.get(url, timeout=5)
        features["Redirect"] = 1 if len(r.history) > 1 else -1
    except:
        features["Redirect"] = -1

    # --- 20–22. on_mouseover, RightClick, popUpWidnow ---
    try:
        page = requests.get(url, timeout=5).text
        features["on_mouseover"] = 1 if re.search(r"onmouseover", page, re.I) else -1
        features["RightClick"] = 1 if re.search(r"event.button ?== ?2", page, re.I) else -1
        features["popUpWidnow"] = 1 if re.search(r"alert\(", page, re.I) else -1
    except:
        features["on_mouseover"] = features["RightClick"] = features["popUpWidnow"] = -1

    # --- 23. Iframe ---
    features["Iframe"] = 1 if re.search(r"<iframe", page, re.I) else -1

    # --- 24. age_of_domain ---
    try:
        w = whois.whois(domain)
        crt = w.creation_date
        if isinstance(crt, list): crt = crt[0]
        if crt:
            age = (datetime.now() - crt).days
            features["age_of_domain"] = 1 if age > 180 else -1
        else:
            features["age_of_domain"] = -1
    except:
        features["age_of_domain"] = -1

    # --- 25. DNSRecord ---
    try:
        socket.gethostbyname(domain)
        features["DNSRecord"] = 1
    except:
        features["DNSRecord"] = -1

    # --- 26–30. web_traffic, Page_Rank, Google_Index, Links_pointing_to_page, Statistical_report ---
    # These need external APIs → placeholders
    features["web_traffic"] = -1
    features["Page_Rank"] = -1
    features["Google_Index"] = -1
    features["Links_pointing_to_page"] = -1
    features["Statistical_report"] = -1

    # ✅ Ensure DataFrame in correct column order
    expected_cols = [
        "having_IP_Address", "URL_Length", "Shortining_Service",
        "having_At_Symbol", "double_slash_redirecting", "Prefix_Suffix",
        "having_Sub_Domain", "SSLfinal_State", "Domain_registeration_length",
        "Favicon", "port", "HTTPS_token", "Request_URL", "URL_of_Anchor",
        "Links_in_tags", "SFH", "Submitting_to_email", "Abnormal_URL",
        "Redirect", "on_mouseover", "RightClick", "popUpWidnow", "Iframe",
        "age_of_domain", "DNSRecord", "web_traffic", "Page_Rank",
        "Google_Index", "Links_pointing_to_page", "Statistical_report"
    ]

    df = pd.DataFrame([[features.get(col, -1) for col in expected_cols]], columns=expected_cols)
    return df
