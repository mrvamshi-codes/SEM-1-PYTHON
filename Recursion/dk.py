def process_data(data,callback):
	result=[d*2 for d in data]
	callback(result)               #call the callback function with the result


def print_result(result):
	print("processed data:",result)


data =[1,2,3]
process_data(data,print_result)


#output -- processed data: [2, 4, 6]