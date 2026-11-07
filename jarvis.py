import google.generativeai as genai
import pyautogui

# Initialize Gemini API
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def run_jarvis():
    print("Jarvis 0.2 Automation Initialized")
    pyautogui.screenshot("screen_state.png")

if __name__ == "__main__":
    run_jarvis()
