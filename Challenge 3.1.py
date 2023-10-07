def linear_search_product(productlist,targetproduct):
 indices=[] 

 for index, product in enumerate(productlist):
    if product== targetproduct:
      indices.append(index)
  
 return indices

#input values
products=["apple","one_plus","realmi","apple","samsung","apple","one_plus"]
target="apple"
result=linear_search_product(products,target)
print(result)
