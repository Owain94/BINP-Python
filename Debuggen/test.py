def main():
    prev = 1
    for i in range(9999, 99999999):
        prev = prev * i
        print(prev)

if __name__ == '__main__':
    main()