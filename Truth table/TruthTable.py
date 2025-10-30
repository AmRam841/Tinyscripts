from itertools import product





def Truth_table(variables , formula):
    print(" | " .join(variables) + " | Result" )# prints the lines between vars
    print("-" *( 4 * len(variables) + 9) )# prints the line beneeth the vars and result 
# we have to have 2 arguments with this one . first one the number of state a variable can be in , in this case 2
# secoond repeat means how many times it is going to make groups and try all the combinations 
    for values in product([True , False] , repeat=len(variables)): 
        eval_env = dict(zip(variables , values))
        try:
            result = eval(formula , {} , eval_env )
        except Exception as e:
                print(f"err evaluting formula : {e}")
                return
        row = " | ".join(['1' if v else '0' for v in values]) + " | " + ('1' if result else '0') 
        print(row)
    
if __name__ == "__main__" : # for making this useable for anyone who wants to import , the name is equal to main when its directly executed 
     vars = input("enter varrs : ").replace(" ","").split(",")
     formula = input("Give me the fromula using python logic : ")
     Truth_table(vars,formula)

     


        



















