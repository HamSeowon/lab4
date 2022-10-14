def helloWorld():
    print("hellow world")

def helloWorldTimes(n):
    for i in range(n):
        helloWorld()

def main():
    helloWorldTimes(2)
    helloWorldTimes(1)
    helloWorldTimes(3)
    helloWorldTimes(2)

main()
