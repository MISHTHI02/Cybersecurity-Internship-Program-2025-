
import unicodedata
import difflib

# List of safe domains to compare against
SAFE_DOMAINS = [
    "google.com", "amazon.com", "facebook.com", "paypal.com", "microsoft.com", "youtube.com"
]

# Function to normalize Unicode domain to ASCII-like form
def normalize_domain(domain):
    return unicodedata.normalize('NFKC', domain)

# Function to detect similarity
def is_suspicious(domain, safe_domains):
    for safe in safe_domains:
        similarity = difflib.SequenceMatcher(None, domain, safe).ratio()
        if similarity > 0.9 and domain != safe:
            return True, safe, similarity
    return False, "", 0.0

def main():
    print("🔍 Homoglyph Detector - Type a domain (or 'exit' to quit)")
    while True:
        user_input = input("\nEnter a domain to check (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            break
        normalized = normalize_domain(user_input)
        print(f"🔍 Normalized domain: {normalized}")
        suspicious, matched, score = is_suspicious(normalized, SAFE_DOMAINS)
        if suspicious:
            print(f"⚠️ WARNING: '{user_input}' looks like '{matched}' (similarity: {score:.2f})")
        elif normalized in SAFE_DOMAINS:
            print("☑️ This domain looks safe.")
        else:
            print("⚠️ Unknown domain. Use with caution.")

if __name__ == "__main__":
    main()
