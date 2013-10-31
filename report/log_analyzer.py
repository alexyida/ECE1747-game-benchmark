import matplotlib.pyplot as plt

f0 = open("/Users/alexyida/report/static_random.txt", "r")
f1 = open("/Users/alexyida/report/static_quest.txt", "r")
f2 = open("/Users/alexyida/report/lightest_random.txt", "r")
f3 = open("/Users/alexyida/report/lightest_quest.txt", "r")

f_list = [f0, f1, f2, f3]

i = 0
for f in f_list:
    requests = {0:[[], []], 1:[[], []], 2:[[], []], 3:[[], []]}
    updates = {0:[[], []], 1:[[], []], 2:[[], []], 3:[[], []]}    
    for l in f:
        parts = l.split(",")
        
        iteration = int(parts[0].split()[-1])
        tid = int(parts[1].split()[-1])
        number = int(parts[2].split()[-1])
        duration = int(parts[3].split()[-1])
        
        # ignore the first 200 iterations because during which client are joining
        # total number of iterations in the chart will be 10000
        if iteration >= 200 and iteration < 10200: 
            if parts[2].split()[-2] == "requests:":
                requests[tid][0].append(number)
                requests[tid][1].append(duration)
            else:
                updates[tid][0].append(number)
                updates[tid][1].append(duration)            
    
    f.close()

    title = ""
    if i == 0:
        title = "Static algorithm without quest"
    elif i == 1:
        title = "Static algorithm with quest"
    elif i == 2:
        title = "Lightest algorithm without quest"
    elif i == 3:
        title = "Lightest algorithm with quest"

    plt.plot(requests[0][0])
    plt.plot(requests[1][0])
    plt.plot(requests[2][0])
    plt.plot(requests[3][0])
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('# of requests')
    if i == 0:
        plt.savefig("static-random-request-number.png")
    elif i == 1:
        plt.savefig("static-quest-request-number.png")
    elif i == 2:
        plt.savefig("lightest-random-request-number.png") 
    elif i == 3:
        plt.savefig("lightest-quest-request-number.png")  
    
    plt.clf()
    
    plt.plot(requests[0][1])
    plt.plot(requests[1][1])
    plt.plot(requests[2][1])
    plt.plot(requests[3][1])
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('processing time')
    if i == 0:
        plt.savefig("static-random-request-time.png")
    elif i == 1:
        plt.savefig("static-quest-request-time.png")
    elif i == 2:
        plt.savefig("lightest-random-request-time.png")
    elif i == 3:
        plt.savefig("lightest-quest-request-time.png")  
    
    plt.clf()
    
    plt.plot(updates[0][0])
    plt.plot(updates[1][0])
    plt.plot(updates[2][0])
    plt.plot(updates[3][0])
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('# of updates')
    if i == 0:
        plt.savefig("static-random-update-number.png")
    elif i == 1:
        plt.savefig("static-quest-update-number.png")
    elif i == 2:
        plt.savefig("lightest-random-update-number.png")
    elif i == 3:
        plt.savefig("lightest-quest-update-number.png")  
    
    plt.clf()
    
    plt.plot(updates[0][1])
    plt.plot(updates[1][1])
    plt.plot(updates[2][1])
    plt.plot(updates[3][1])
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('sending time')
    if i == 0:
        plt.savefig("static-random-update-time.png")
    elif i == 1:
        plt.savefig("static-quest-update-time.png")   
    elif i == 2:
        plt.savefig("lightest-random-update-time.png")
    elif i == 3:
        plt.savefig("lightest-quest-update-time.png")  
    
    plt.clf()
    i += 1