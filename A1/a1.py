import re

data_set_size = 10000

"{:.3f}".format(5)

to_read = open("IRAhandle_tweets_1.csv", "r", encoding="utf-8")

#resetting dataset.tsv contents before writing
data_tsv1 = open("dataset.tsv", "w");
data_tsv1.write("tweet_id  publish_date    content  trump_mention\n")
data_tsv1.close()

#resetting results.tsv contents before writing
results_tsv_reset = open("results.tsv", "w", encoding="utf-8")
results_tsv_reset.write("result value\n")
results_tsv_reset.close()

#reopening file for appending
data_tsv = open("dataset.tsv", "a", encoding='utf-8');

data = to_read.readline()

for x in range(data_set_size):

    data = to_read.readline()

    seperated = data.split(",")
    list_length = len(seperated)

    content_string = ""
    content_length = list_length-17-1-2

    for y in range(content_length):
        content_string = content_string + "," + seperated[2+y]
    

    #if langauge is English and content does not contain '?'
    if seperated[list_length-1-16] == "English" and  re.search(".*\?.*", content_string) == None:

        #if the string "Trump" appears surrounded by non alphanumeric chars
        if re.search("[^0-9A-Za-z]Trump[^0-9A-Za-z]", content_string) != None:
            
            to_save =  seperated[list_length-1-5] + "   " + seperated[list_length-1-15] + " " + content_string + "   T\n"
            data_tsv.write(to_save)

        #trump_mention = F
        else:
            to_save = seperated[list_length-1-5] + "   " + seperated[list_length-1-15] + " " + content_string + "   F\n"
            data_tsv.write(to_save)

to_read.close()
data_tsv.close()

#counting ratio of T:F

data_tsv_count = open("dataset.tsv", "r", encoding='utf-8')

true_counter = 0
total_counter = 0

data_tsv_count.readline()

for line in data_tsv_count:

    total_counter = total_counter + 1

    if re.search("T$", line) != None:
        true_counter = true_counter + 1

data_tsv_count.close()

if total_counter == 0:
    print("no results")
else:

    result_val = round(true_counter/total_counter, 3)
    results_tsv = open("results.tsv", "a")
    results_tsv.write("frac_trump_mentions  " + str(result_val))
    results_tsv.close()