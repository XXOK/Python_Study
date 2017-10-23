if __name__ == '__main__':

    naver_end_price = [474500, 461500, 501000, 500500, 488500]
    naver_end_price2 = {'09/07' : 474500, '09/08' : 461500, '09/09' : 501000, '09/10' : 500500, '09/11' : 488500}

    maxp = max(naver_end_price)
    minp = min(naver_end_price)

    print(naver_end_price)

    print("MAX: ", maxp, "/ MIN: ", minp)

    print("MAX - MIN: ", maxp-minp)

    print("수요일 종가: ", naver_end_price[2])

    print("09/09의 종가: ", naver_end_price2['09/07'])
