import os


def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    count = 0
    for candle in candles:
        if candle == tallest_candle:
            count += 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
