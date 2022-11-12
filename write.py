import csv
from sportclub import SportClub
from typing import List, Iterable
from operator import itemgetter, attrgetter

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"),
        SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"),
        SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    
    
    sorted_clubs = {}
    
    for team in all_clubs:
        if team.sport in sorted_clubs:
            sorted_clubs[team.sport].append(team)
        else:
            sorted_clubs[team.sport] = [team]

    sorted_clubs = list(sorted_clubs.values())

    #for i in all_clubs:
        #print(i)

    #for i in sorted_clubs:
        #for j in i:
            #print(j)

    #print(all_clubs)
    #print()
    #print(sorted_clubs)

    return sorted_clubs
    
    


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80),
        SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130),
        SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    
    count_sort = sorted(sport, key=lambda x: (-x.count,x.name))
    
    #s = sorted(sport, key=attrgetter('name'))
    #sorted(s, key=attrgetter('count'), reverse=True)

    #sorted(sport, key=attrgetter('count','name'))
    #sport.reverse()

    
    for i in count_sort:
        print(i)
            
    
    return count_sort


    
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    #return []  erase this


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    #for i in sorted_sports:
        #for j in i:
            #print(j)


    
    with open('survey_database.csv', 'w', newline='') as myCSVFile:
        writeToMyCSV = csv.writer(myCSVFile)   
    
        writeToMyCSV.writerow(['City','Team Name', 'Sport','Number of Times Picked'])

        for sport in sorted_sports:
            if len(sport) >= 3:
                for num in range(3):
                    writeToMyCSV.writerow([sport[num].city, sport[num].name, sport[num].sport, sport[num].count])
            else:
                for num in range(len(sport)):
                    writeToMyCSV.writerow([sport[num].city, sport[num].name, sport[num].sport, sport[num].count])
    

        
    # TODO: Complete the function
    #pass  erase this

sortSport([SportClub("Houston", "Rockets", "NBA", 80), SportClub("La", "Niharika", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)])
