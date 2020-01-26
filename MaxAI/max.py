import wolframalpha
import wikipedia

while True:
    question = input("Question: ")
    try:
        app_id = "25V5HT-82PKXXEAE3"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print (answer)
    except:
        print(wikipedia.summary(question))

# Question is queryed through wolframalpha if wolfram fails, 
# question is passed to wikipedia and exception is wiki summary.
