from document_loader import load_document


if __name__ == "__main__":

    file_path = input("Enter document path: ")

    try:
        extracted_text = load_document(file_path)

        print("\n========== EXTRACTED TEXT ==========\n")
        print(extracted_text)

        print("\n=========== SUMMARY ===========")
        print("Document loaded successfully!")

    except Exception as e:
        print(f"Error: {e}")