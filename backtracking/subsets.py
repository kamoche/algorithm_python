def subsets(nums):
     result = []

     sub_sets = []
     def dfs(index):
          print(f'curent index {index} result list = { result}')
          if index >= len(nums):
               result.append(sub_sets.copy())
               return
          #decision to include nums[index]
          print("============> ", nums[index])        
          sub_sets.append(nums[index])
          dfs(index + 1)
            # decision not to include nums[index]
          print("pop number => ", str(sub_sets.pop()))
          dfs(index + 1)
     dfs(0)

     return result


     
print(subsets([1,2,3]))

     





            