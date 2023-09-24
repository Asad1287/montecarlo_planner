import csv as csv
from scipy.stats import norm
import numpy as np
import os 
from charts import *
import argparse
import sys
import os

# Get the current script's directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Append the parent directory to sys.path
sys.path.append(parent_directory)

from models.approximation.generate_summaries import *
from excel.reader import *
from simulation.simple_monte_carlo import *
from typing import List,Dict

#write a function which takes in list of lists, and samples from each nested list in each iteration 

#get command line arguments


def lists_sampling(list_of_lists:List[List[float]],iterations:int=100000) -> List[float]:
    final_list = []
    for _ in range(iterations):
       #for each of the list randomly select an element and append it to final_list
       temp_list = [] 
       for j in range(len(list_of_lists)):
           temp = np.random.choice(list_of_lists[j],1)
           #convert temp to float
           temp = float(temp)
           temp_list.append(temp)
           
          
       final_list.append(sum(temp_list))
    return final_list

def csv_reader_row_wise(input_file:str,output_file:str,aggregate:bool=False,sheet_name=None,table_name=None,aggregation_iterations:int=100) -> List[float]:
    #check input_file extension
    file_extension = os.path.splitext(input_file)[1]
    if file_extension == '.csv':
        csv_url = input_file
    elif file_extension == '.xlsx':
        df = read_excel_table(input_file,sheet_name,table_name)
        #write df to csv
        df.to_csv(output_file,index=False)
        csv_url = output_file
    else:
        print("Invalid file type")
        return
    
    results_list = []
    
    with open(csv_url, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Results']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            expression = row['Expression']
            variable_distributions = {
                'Variable1': row['Variable1'],
                'Variable2': row['Variable2']
            }
            results = monte_carlo_runner(expression, variable_distributions)
            results_list.append(results)
            row['Results'] = describe_distribution(results)
            writer.writerow(row)
    if aggregate:
        final_list = lists_sampling(results_list,aggregation_iterations)
    else:
        return results_list
    
    chart_output(final_list,save_location=".",chart_title="chart")
    
    return final_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monte Carlo Planner')

    
    parser.add_argument('input_file', help='The input file.')
   
    parser.add_argument('output_file', help='The output file.',default='output.csv',nargs='?')
    parser.add_argument('sheet_name', help='The sheet name.',default=None,nargs='?')    
    parser.add_argument('table_name', help='The table name.',default=None,nargs='?')
    args = parser.parse_args()

    # Set default values for arguments, if not provided.
    
    if args.input_file is None:
        raise ValueError("Input file not provided.")
   
    args.input_file = args.input_file 
    args.output_file = args.output_file 
    args.sheet_name = args.sheet_name 
    args.table_name = args.table_name 
    csv_reader_row_wise(args.input_file,args.output_file,sheet_name=args.sheet_name,table_name=args.table_name)



