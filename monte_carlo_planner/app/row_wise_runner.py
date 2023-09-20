import csv as csv
from scipy.stats import norm
import numpy as np
from charts import *




#write a function which takes in list of lists, and samples from each nested list in each iteration 

def lists_sampling(list_of_lists,iterations):
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

def csv_reader_row_wise(csv_url,output_file,aggregate=False,aggregation_iterations=100000):
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
    
    return final_list


csv_url = 'D:\\RealProject\\capital_planning_simulator\\SampleData\\risk_data.csv'


output_file =  'output.csv'

final_list = csv_reader_row_wise(csv_url,output_file,aggregate=True,aggregation_iterations=100000)

chart_output(final_list,save_location=".",chart_title="chart")