import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("=" * 55)
        print("        🚀 ODYSSEUS 2.0 STUDENT AUTOMATION PACK 🚀        ")
        print("=" * 55)
        print("  [1] Tailor Resume (Runs local Qwen LLM Core)")
        print("  [2] Triage Email Inbox (Check Confirmations)")
        print("  [3] Initialize/Verify Local Database Engine")
        print("  [4] Exit Suite")
        print("=" * 55)
        
        choice = input("Select an engine utility option [1-4]: ").strip()
        
        if choice == '1':
            print("\n")
            os.system("python backend\\tailor_engine.py")
            input("\nPress Enter to return to Main Menu...")
        elif choice == '2':
            print("\n")
            os.system("python backend\\email_parser.py")
            input("\nPress Enter to return to Main Menu...")
        elif choice == '3':
            print("\n")
            os.system("python backend\\database_engine.py")
            input("\nPress Enter to return to Main Menu...")
        elif choice == '4':
            print("\nExiting Odysseus 2.0 Core Interface. Happy Engineering!")
            sys.exit()
        else:
            input("\n❌ Invalid selection. Press Enter to retry...")

if __name__ == "__main__":
    main_menu()