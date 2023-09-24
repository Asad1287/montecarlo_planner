import pandas as pd 
from typing import List , Dict
import numpy as np
from scipy.stats import norm, expon, lognorm, weibull_min, gamma
from charts import *
from scipy import stats
import argparse
import sys
import os

# Get the current script's directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Append the parent directory to sys.path
sys.path.append(parent_directory)
from distr_parser.parserfunction import *


def apply_parsing_to_vector(vector:List[str]):
    return [parse_distribution(distr_str) for distr_str in vector]

#test apply_parsing_to_vector
test_vector = ['NORM(10,1)','NORM(20,2)','NORM(30,3)']
print(f"apply_parsing_to_vector_test_vector: {test_vector}")

def generate_rvs_in_list(vector:List[stats._distn_infrastructure.rv_frozen],iterations:int=1):
    temp = [vector.rvs(iterations) for vector in vector]
    #flatten temp 
    result = [item for sublist in temp for item in sublist]
    return result

#test generate_rvs_in_list
test_vector = ['NORM(10,1)','NORM(20,2)','NORM(30,3)']
test_parsed_vector = apply_parsing_to_vector(test_vector)
test_result = generate_rvs_in_list(test_parsed_vector)
print(f"test_result_generate_rvs_in_list: {test_result}")

def apply_operator_two_vectors(vector1:List[float],vector2:List[float],operator:str='+'):
    if operator == '+':
        for i in range(len(vector1)):
            vector1[i] = vector1[i] + vector2[i]
        return vector1
    elif operator == '-':
        for i in range(len(vector1)):
            vector1[i] = vector1[i] - vector2[i]
        return vector1
    elif operator == '*':
        for i in range(len(vector1)):
            vector1[i] = vector1[i] * vector2[i]
        return vector1
    elif operator == '/':
        for i in range(len(vector1)):
            vector1[i] = vector1[i] / vector2[i]
        return vector1
    else: 
        raise ValueError(f"Unknown operator type: {operator}")



#test apply_operator_two_vectors
test_vector1 = [1,2,3]
test_vector2 = [4,5,6]
test_operator = '+'
test_result = apply_operator_two_vectors(test_vector1,test_vector2,test_operator)
print(f"test_result: {test_result}")
    
def apply_operator_to_list_of_vectors(list_of_vectors:List[List[float]],operator_list:List[str]):
    # Initialize an array for the accumulated result
    accumulated_result = np.zeros(len(list_of_vectors[0]))
    
    #assert all vectors are the same length
    for vector in list_of_vectors:
        assert len(vector) == len(accumulated_result)
    #assert that operator list is one less than the number of vectors
    

    # Initialize the first vector as the accumulated result
    accumulated_result = list_of_vectors[0]

    # Go through the other vectors and apply the operations
    for vector, operator in zip(list_of_vectors[1:],operator_list):
        accumulated_result = apply_operator_two_vectors(accumulated_result,vector,operator)

    return accumulated_result

#test apply_operator_to_list_of_vectors
test_list_of_vectors = [[1,2,3],[4,5,6],[7,8,9]]
test_operator_list = ['+','+']
test_result = apply_operator_to_list_of_vectors(test_list_of_vectors,test_operator_list)
print(f"test_result: {test_result}")

input_object = {
        'vector':[['NORM(10,1)','NORM(20,2)','NORM(30,3)'],['NORM(40,4)','NORM(50,5)','NORM(60,6)'],['NORM(40,4)','NORM(50,5)','NORM(60,6)']],
        'operations': ['+','+']
        }

def run_simulations(input_dict_vector_operations:Dict[List[List[str]],List[str]],iterations:int=1):
    temp_list = []
    aggregated_result = []
    aggregated_sum = []
    for _ in range(iterations):
        for vector in input_dict_vector_operations['vector']:
            parsed_list = apply_parsing_to_vector(vector)
            rvs_list = generate_rvs_in_list(parsed_list,1)
            temp_list.append(rvs_list)
        aggregated_result.append(apply_operator_to_list_of_vectors(temp_list,input_dict_vector_operations['operations']))
        aggregated_sum.append(sum(aggregated_result[-1]))
        temp_list = []
    #flatten aggregated_result
    return aggregated_sum

#test run_simulations
test_input_object = {
        'vector':[['NORM(10,1)','NORM(10,1)','NORM(10,1)'],['NORM(10,1)','NORM(10,1)','NORM(10,1)'],['NORM(10,1)','NORM(10,1)','NORM(10,1)']],
        'operations': ['+','+']
        }



def csv_to_dict(file_name: str) -> dict:
    # Read the csv into a pandas DataFrame
    df = pd.read_csv(file_name)
    
    # Convert the DataFrame into the desired dictionary structure
    vector = df[['Var1', 'Var2', 'Operation']].values.tolist()
    
    # Separate operations from the vectors
    operations = [row.pop(-1) for row in vector]
    
    # Prepare the final dictionary
    input_object = {
        'vector': vector,
        'operations': operations[:-1]  # The last operation is not needed based on the provided example
    }
    
    return input_object



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monte Carlo Planner')

    
    parser.add_argument('input_file', help='The input file.')
   
   
    args = parser.parse_args()

    # Set default values for arguments, if not provided.
    
    
    args.input_file = args.input_file 
   
    input_object = csv_to_dict(args.input_file)
    test_result = run_simulations(input_object,iterations=1000)
    

    chart_output(test_result)

