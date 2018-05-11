print([x*2 for x in range(1,11)])
print(list(map(lambda x:x*2,range(1,11))))
wordlist = ["scala", "akka", "play framework", "sbt", "typesafe"]

tweet = "This is an example tweet talking about scala and sbt."

print(list(filter(lambda x: x in tweet.split(), wordlist)))