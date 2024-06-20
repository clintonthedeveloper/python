try:
    result = 1 / 0
    print(1 /0)
except ZeroDivisionError as e :

    # code to handle exception
    print(f"An Error has occurred: {e}")
finally:

    # code that runs no matter what
    print("This will always be printed")

    #
jina=['banana', 'apple', 'orange', 'bajia']
try:
 for i in range(5):
     print(jina[i])
except:
    print("An error has occurred")

