#!/usr/bin/env python

import time
from __future__ import division
import requests
from collections import Counter


def checker():
    def send_get():
        #GET to the endpoint to receieve the JSON data
        print('sending request')
        r  = requests.get('http://54.88.56.68/api/v2/profiles/3')

        # Opens the JSON data and sets it to the "data" variable
        data = r.json()

        # Prints the data in the Console.
        print data #NOTE:(COLIN) Remove this before production.
        data[one]
        data[two]
        return(data)

    # Take the (a, b) and run an intersection too find the ones that match.
    def count_matches(a, b):
        print('counting matches')
        cnt = Counter(a)
        cnt2 = Counter(b)
        keys = set(a).intersection(b)

        # Sets total_matches to 0
        total_matches = 0

        # Gives an empty object for the "both"
        both = {}
        for key in keys:
            smallest = min(cnt[key], cnt2[key])
            both[key] = smallest
            total_matches += smallest
        return keys, total_matches, both

    def main():
        data = send_get()
        for one, two in data:
            keys, total_matches, both = count_matches(one, two)
            print 'Values in Both: {}'.format(keys)
            print 'Values with their totals:'
            for k, v in both.iteritems():
                print '\tKey: {}\tTotal_Matches: {}'.format(k, v)
            print 'Total Matches: {}'.format(total_matches)
            print '-------\n'
            match = int(total_matches)
            key_val = len(two)
            wynbi_score = int(match) / int(key_val) * 100
            print wynbi_score
            print '-------\n'
    main()

if __name__ == '__main__':
    while True:
        checker()
        time.sleep(1)
#assert count_matches(data, data_two)

# Returns the match count found in the intersection ie.(5)

# If there are no matches found, print that.
# Else send data to the endpoint for storage and pickup
#if(total_value = 0):
#    print "not matches found" #NOTE:(Colin) Remove this before production and send back in POST.
#else:
#    endpoint = 'http://54.88.56.68/api/v2/some-endpoint    '
#    data_json = json.dumps(total_value)
#    requests.post(endpoint, data_json)
#    print "success" #NOTE:(Colin) Remove this before production and send back in POST.
