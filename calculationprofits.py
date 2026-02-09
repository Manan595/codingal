def calculateprofits(arr,arr_size):
    profit=0
    for i in range(1,arr_size):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]

        return profit
pricesofsevendays=[635,678,890,2345,768,654,123]
profit = calculateprofits(pricesofsevendays,len(pricesofsevendays))
print('max profit :',profit)
