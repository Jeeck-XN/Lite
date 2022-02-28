#GNU nano 6.0                         run.py
if __name__ == "__main__":
        try:
                __import__("Lite").menu()
        except Exception as e:
                exit(str(e))
