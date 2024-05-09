import pyodbc
server_name = "DESKTOP-DLFEC7O\SQLEXPRESS"
database_name = "HexawareMoviesDB"
 

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("Select 1")
print("Database connection is successful 🎊")
 
def read_moviesI():
    cursor.execute("select * from movies")
    #movies=cursor.fetchall()   #get all data
    # for movie in movies:
    #     print(movie)
    
    #get data one row at a time
    for row in cursor:
        print(row)
print("Welcome to the movies app")

# Task 1
# Get the data from the user
# Clue: Use arguments
def create_movie():
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        ("Oppenheimer", 2023, 1),
    )
    conn.commit()  # Permanent storing | If no commit then no data
 
 
# Task 2
# Delete a movie from the db by getting the id from user
def delete_movie(movie_id):
    pass
 
if __name__ == "__main__":
    create_movie()
    read_movies()
 
#  CRUD -Create,Read,Update,Delete
#  Task 3 and 4
# Menu:
#     "1. Create a movie"
#     "2. View all"
#     "3. Update a movie"
#     "4. Delete a movie"
#     "5. Exit"
   
choice=int(input("please enter a choice:"))

if(choice==1):
    title=input("please enter movie title:")
    year=int(input("please enter movie year:"))
    director_id=int(input("please enter movie  director_id:"))
    create_movie(title,year,director_id)
elif(choice==2):
    read_movies()
elif(choice==3):
    movie_id_to_update = input("Enter the ID of the movie you want to update: ")
    title = input("Enter the updated movie title: ")
    year = input("Enter the updated release year: ")
    director_id = input("Enter the updated director ID: ")
    update_movie(movie_id_to_update, title, year, director_id)
 
elif(choice==4):
    movie_id=int(input("please enter movie  movie_id:"))
    delete_movie(movie_id)
elif(choice == 5):
    print("Exit the program.")
    break
 
else:
    print("enter a valid option.")



# TASK 5
## keep it in loop
 
 
def update_movie(movie_id, title, year, director_id):
    cursor.execute(
        "UPDATE Movies SET Title = ?, Year = ?, DirectorId = ? WHERE MovieId = ?",
        (title, year, director_id, movie_id)
    )
    conn.commit()
    print("Movie updated successfully!")
 
 
def menu():
    print("\nMenu:")
    print("1. Create a movie")
    print("2. Update a movie")
    print("3. Delete a movie")
    print("4. Exit")
 
 
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")
 
        if choice == "1":
            title = input("Enter the movie title: ")
            year = input("Enter the release year: ")
            director_id = input("Enter the director ID: ")
            create_movie(title, year, director_id)
            print("Movie added successfully!")
 
        elif choice == "2":
            read_movies()
            movie_id_to_update = input("Enter the ID of the movie you want to update: ")
            title = input("Enter the updated movie title: ")
            year = input("Enter the updated release year: ")
            director_id = input("Enter the updated director ID: ")
            update_movie(movie_id_to_update, title, year, director_id)
 
        elif choice == "3":
            read_movies()
            movie_id_to_delete = input(" ID of the movie to delete: ")
            delete_movie(movie_id_to_delete)
 
        elif choice == "4":
            print("Exit the program.")
            break
 
        else:
            print("enter a valid option.")