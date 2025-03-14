import json
import os

# 📂 File where library data is stored
LIBRARY_FILE = "library_data.json"

def load_library():
    """📥 Loads the library from a file, returning an empty list if the file doesn't exist or is unreadable."""
    if not os.path.exists(LIBRARY_FILE):
        return []
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_library(library):
    """💾 Saves the library data to a file in JSON format."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def print_header(title):
    """🎀 Prints a formatted header with the given title."""
    print("\n" + "✨" * 50)
    print(f"📚 {title} 📚".center(50))
    print("✨" * 50)

def add_book(library):
    """📝 Prompts user for book details and adds the book to the library."""
    print_header("➕ Add a Book")
    book = {
        "Title": input("📖 Title: "),
        "Author": input("✍️ Author: "),
        "Year": int(input("📅 Publication Year: ")),
        "Genre": input("📚 Genre: "),
        "Read": input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes",
        "Rating": float(input("⭐ Rate the book (1-5): "))
    }
    library.append(book)
    print("🎉✅ Book successfully added to your library!")

def remove_book(library):
    """🗑️ Removes a book from the library by title."""
    print_header("🗑️ Remove a Book")
    title = input("🔻 Enter the book title to remove: ")
    original_count = len(library)
    library[:] = [book for book in library if book["Title"].lower() != title.lower()]
    print("🗑️✅ Book successfully removed!" if len(library) < original_count else "❌ Book not found. Try again!")

def search_books(library):
    """🔎 Searches for books by title or author."""
    print_header("🔍 Search for a Book")
    query = input("🔎 Enter title or author: ").strip().lower()
    results = [b for b in library if query in b["Title"].lower() or query in b["Author"].lower()]
    if results:
        print("🎯 Matching Books:")
        for idx, book in enumerate(results, 1):
            print(f"{idx}. 📖 {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'✅ Read' if book['Read'] else '❌ Unread'} - ⭐ {book['Rating']}/5")
    else:
        print("❌ No matches found. Try a different search!")

def display_books(library):
    """📖 Displays all books currently in the library."""
    print_header("📚 All Books in Library")
    if not library:
        print("📭 Your library is empty! Add books to get started.")
    else:
        for idx, book in enumerate(library, 1):
            print(f"{idx}. 📖 {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'✅ Read' if book['Read'] else '❌ Unread'} - ⭐ {book['Rating']}/5")

def display_stats(library):
    """📊 Displays statistics about the library such as total books, percentage read, and average rating."""
    print_header("📊 Library Statistics")
    total = len(library)
    read_books = sum(1 for book in library if book["Read"])
    avg_rating = sum(book["Rating"] for book in library) / total if total else 0
    print(f"📚 Total Books: {total}\n✅ Books Read: {read_books} ({(read_books / total * 100) if total else 0:.2f}%)\n⭐ Average Rating: {avg_rating:.2f}/5")

def recommend_books(library):
    """🎯 Recommends books that haven't been read yet, sorted by highest rating."""
    print_header("🎯 Recommended Books")
    unread_books = [book for book in library if not book["Read"]]
    if not unread_books:
        print("🎉 You've read all books! Add more to get recommendations.")
    else:
        print("📌 Suggested Books:")
        for idx, book in enumerate(sorted(unread_books, key=lambda x: x["Rating"], reverse=True), 1):
            print(f"{idx}. 📖 {book['Title']} by {book['Author']} - ⭐ {book['Rating']}/5")

def library_manager():
    """🎮 Main function that runs the interactive menu for managing the personal library."""
    library = load_library()
    menu_options = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": display_stats,
        "6": recommend_books,
        "7": lambda x: print("👋 Exiting and saving... Have a great day! 🌟")
    }
    while True:
        print_header("📖 Library Manager")
        print("1️⃣ Add Book\n2️⃣ Remove Book\n3️⃣ Search Books\n4️⃣ Show All Books\n5️⃣ Show Stats\n6️⃣ Get Book Recommendations\n7️⃣ Exit")
        choice = input("🎯 Choose an option: ")
        if choice == "7":
            break
        action = menu_options.get(choice)
        if action:
            action(library)
        else:
            print("❌ Invalid choice. Please try again!")
    save_library(library)

library_manager()
