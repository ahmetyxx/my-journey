# with open("my_text.txt") as document:
#     content=document.read()
#     print(content)
    
# with open("my_text.txt", mode="w") as document:
#     document.write("no i hate to write")

        
with open(r"\docs\projects\Engineering-Lab\python-courses\my_text.txt", mode="r") as document:
    print(document.read())