import difflib

# Report function
def generate_report(links, suspicious_links):
    print("\n✅ Links Found ({}):".format(len(links)))
    for link in links:
        print("   -", link)

    print("\n⚠️ Suspicious (potentially fake) links:")
    if suspicious_links:
        for s_link in suspicious_links:
            print("   -", s_link)
    else:
        print("   None detected")


# Normalize domain to ASCII for comparison
def normalize_domain(domain):
    try:
        return domain.encode("idna").decode("ascii")  # Convert Unicode to punycode if needed
    except Exception:
        return domain


# Check if a domain is suspicious compared to target
def is_suspicious(domain, target, similarity_threshold=0.8):
    normalized_domain = normalize_domain(domain)
    normalized_target = normalize_domain(target)

    similarity = difflib.SequenceMatcher(None, normalized_domain, normalized_target).ratio()
    return normalized_domain != normalized_target and similarity >= similarity_threshold


# Main script
if __name__ == "__main__":
    target_domain = "youtube.com"
    links_to_check = [
        "https://youtube.com",       # Legit
        "https://yoυtube.com",       # Greek upsilon instead of 'u'
        "https://youtubee.com",      # Extra letter
        "https://example.com"        # Unrelated
    ]

    suspicious_links = [
        link for link in links_to_check if is_suspicious(link.replace("https://", ""), target_domain)
    ]

    generate_report(links_to_check, suspicious_links)
