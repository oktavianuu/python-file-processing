Refactoring is a very important process during software development. The main purpose of refactoring is to improve the quality of the code. Every programmer in their career will have to refactor either their own or someone else’s code sooner or later.

A very common mistake made by young adepts of the art of programming is to repeat the same pieces of code in different places in the application. In this case, refactoring consists of creating a function containing repetitive fragments. As a result, the code’s volume is reduced, and it becomes more readable.

We've probably noticed that adding new functionalities to our TODO application would be very difficult. This is a sign that our application requires refactoring. Below are suggestions for changes we can make:
1. creating a class called TODO that will connect to the database in the constructor. If you want, you can implement a separate method called connect for this purpose;
2. moving the code responsible for creating the taskstable to the method named create_tasks_table;
3. creating a method called add_task that will get the task name and priority from the user instead of using hardcoded values.

Will we be able to easily implement, for example, the data display functionality after these changes?