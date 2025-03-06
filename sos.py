import random

def get_sos_resources(location=None):
    resources = {
        "India": [
            {"name": "Vandrevala Foundation", "contact": "1860 266 2345"},
            {"name": "iCall", "contact": "+91 9152987821"},
            {"name": "Snehi", "contact": "+91-9582208181"},
            {"name": "Sumaitri (Delhi)", "contact": "+91 11 23389090"},
            {"name": "Samaritans Mumbai", "contact": "+91 8422984528"},
            {"name": "AASRA", "contact": "91-9820466726"},
            {"name": "Connecting Trust", "contact": "+91 9922001122"},
        ],
        "Online": [
            {"name": "NIMHANS", "contact": "https://www.nimhans.ac.in/"},
            {"name": "AASRA", "contact": "http://www.aasra.info/"},
            {"name": "YourDOST", "contact": "https://yourdost.com/"},
            {"name": "7 Cups", "contact": "https://www.7cups.com/"},
        ]
    }

    if location and location in resources:
        selected_resources = random.sample(resources[location], min(3, len(resources[location])))
    else:
        selected_resources = random.sample(resources["India"], min(3, len(resources["India"])))

    resource_message = "🚨 **Emergency Mental Health Support** 🚨\n\n"
    for resource in selected_resources:
        resource_message += f"📞 **{resource['name']}**: {resource['contact']}\n"

    resource_message += "\n💻 **Online Support:**\n"
    for resource in resources["Online"]:
        resource_message += f"- **{resource['name']}**: {resource['contact']}\n"

    resource_message += "\n🙏 **Aap akelay nahi hain, help ke liye reach out karein!**"
    return resource_message

# Example usage
if __name__ == "__main__":
    print(get_sos_resources("India"))