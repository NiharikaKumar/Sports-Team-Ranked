from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content
    
    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """

    file_content = []

    with open(file,'r',newline='') as f:
        reader = csv.reader(f)
        fields = next(reader)
        
        for line in reader:
            #print(line)
            #print(len(line))

            if '' in line:
                raise ValueError
            else:
                file_content.append(tuple(line[0:3]))


    #print(file_content)
    
    return file_content
            
        
    # TODO: Complete the function
    #return [] erase this


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs
    that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them,
        and accumulates the datagathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the
        number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the
        name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """

    p = Path().glob('*.csv')

    sport_count = []

    num_files = 0
    num_lines = 0
    error_files = []
    #file_names = []
    
    for fileName in p:
        try:
            file_read = readFile(fileName)
            print(file_read)
            
            for sport in file_read:
                obj = SportClub(sport[0], sport[1], sport[2], 1)

                #print(obj)
                
                if obj in sport_count:
                    sport_count[sport_count.index(obj)].incrementCount()
                    ######print(obj.incrementCount())
                else:
                    sport_count.append(obj)
            
            num_files += 1
            num_lines += len(file_read)
            #file_names.append(fileName)
            
        except ValueError:
            error_files.append([fileName])

    with open('report.txt', 'w', newline='') as myReportFile:
        report_csv = csv.writer(myReportFile)

        report_csv.writerow([f'Number of files read: {num_files}'])
        report_csv.writerow([f'Number of lines read: {num_lines}'])
        #report_csv.writerow([f'{file_names}'])

    with open('error_log.txt', 'w', newline='') as myErrorFile:
        error_csv = csv.writer(myErrorFile)
        
        error_csv.writerows(error_files)
    
    
    #for i in sport_count:
        #print(i)
    
    return sport_count
    
    # TODO: Complete the function
    #return []  # erase this

