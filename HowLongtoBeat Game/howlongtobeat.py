from prettytable import PrettyTable
from howlongtobeatpy import HowLongToBeat
import asyncio
while True:
  try:
    inp=input("Enter the Game Name: ")
    
    async def main(inp):
        global results_list
        results_list = await HowLongToBeat().async_search(inp)
    asyncio.run(main(inp)) 

    if results_list is not None and len(results_list) > 0:
        best_element =  max(results_list, key=lambda element: element.similarity)
        table = PrettyTable()
        table.title = best_element.game_name
        table.field_names = ['Game Type', 'Review Score (Out of 100)', 'Main Story Completion Time (in Hrs)','Main Story + Extra Completion Time (in Hrs)','Completionist Time (in Hrs)']
        table.add_row([best_element.game_type,best_element.review_score,best_element.main_story,best_element.main_extra,best_element.completionist])
        print(table)
        break;
    else:
      print("Enter a descriptive Name")      
  except ValueError:
    print("Provide a correct name...")
    continue


