![](https://raw.githubusercontent.com/microsoft/sqlworkshops/master/graphics/microsoftlogo.png)

# Copilot capabilities for SQL database in Microsoft Fabric
In this exercise, you will use **Copilot** to assist with T-SQL queries, including **auto-suggestions**, **fixing error**, and **natural language query** to increase developer efficiency and analyze your data!
There're two ways how to utilize Copilot:
- Inline in the query editor
- By opening a Copilot chat

## Section 1: Using Copilot within the query editor
In the **Query Editor** you can use T-SQL comments as a way to write Copilot prompts. After finishing a prompt press **Enter** or **Space** and Copilot will process your request and suggest SQL code to complete your query. 
There're also other capabilities such as **Explain query** and **Fix query errors**. Let's dive in.

### Task 1.1: Using Copilot within the query editor

1. From the left navigation pane select your workspace.

   <img alt="A picture of a opening a workspace view from the left-side navigation pane." src="../../graphics/Introduction/MirroringOpenWorkspace.png" style="width:600px;">

2. And now select a SQL database item you've created previously (make sure to click on the artifact name).

   <img alt="A picture of a opening a workspace view from the left-side navigation pane." src="../../media/Copilot/SelectDatabaesItem.png" style="width:800px;">

3. Now, select the **New Query** button on the tool bar as you did in previous module.
    
    <img alt="A picture of clicking the New Query button on the tool bar" src="../../graphics/Introduction/ExploreNewQuery.png" style="width:600px;">

4. Copy/Paste the below prompt in the query and press **Enter**. 

   ```
      --Create a query to get the product that is selling the most.
   ```

5. Watch for the loading spinner at the bottom of the editor to track progress, and observe how Copilot’s suggestion appears in the code.

   ![](../../media/copilot-1.png)

   <img alt="A picture of a demonstrating suggested T-SQL query by Copilot." src="../../media/database17.png" style="width:800px;">

   > **Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

   Optional: If you want to continue following the workshop with the exact same query, feel free to copy it

    ```SQL
   SELECT TOP 1
   [P].[Name],
   SUM([SOD].[OrderQty]) AS TotalSold
   FROM [SalesLT].[SalesOrderDetail] AS SOD
   JOIN [SalesLT].[Product] AS P ON SOD.[ProductID] = P.[ProductID]
   GROUP BY P.[Name]
   ORDER BY TotalSold DESC;
   ``` 

7. Press the **Tab** key on your keyboard to accept the suggestion or continue typing to ignore it.

8. Select the query and click on the **Run** icon (or use keyboard shortcut `Ctrl + Enter` or `Shift + Enter`)

   <img alt="A picture of a demonstrating executed query after selecting Run command." src="../../media/database19.png" style="width:800px;">

### Task 1.2: Copilot Quick Actions within the Query Editor

1. Open a new query and paste the following query with a syntax error and click on the **Run** icon.

   ```SQL
   SELECT c.CustomerID, c.FirstName,c.LastName,
      COUNT(so.SalesOrderID) AS TotalPurchases,
      SUM(so.SubTotal) AS TotalSpent,
      AVG(so.SubTotal) AS AverageOrderValue,
      MAX(so.OrderDate) AS LastPurchaseDate
   FROM
      SalesLT.Customer AS c JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID
   GROUP BY c.CustomerID, c.FName, c.LName ORDER BY TotalSpent DESC;

   ```

2. Observe the query errors (issue) and then select **Fix query errors**.

   <img alt="A picture of a demonstrating an issue and finding the Fix Query Errors button in the quick actions next to the Run button in the Query Editor.." src="../../media/Copilot/FixQueryErrors.png" style="width:1200px;">

3. Observe the updated query along with the comment that clearly states where the issue was in the query. Now click on **Run** to see the results.

   <img alt="A picture of a demonstrating added comment at the bottom about what was fixed and query results returned successfully." src="../../media/Copilot/AutoFixComment.png" style="width:1200px;">

  >**Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

4. Aside from fixing the query errors, Copilot can also explain a query to you. Select **Explain query** and Copilot will add comments to your query explaining parts of the query.

   <img alt="A picture of a demonstrating steps to select Explain query and then showing the inline comments in the query editor." src="../../media/Copilot/ExplainQuery.png" style="width:1200px;">

## Section 2: Using Copilot Chat Pane

### Task 2.1: Chat Pane : Natural Language to SQL

1. First open the new query or clear the previous one to have a blank query editor. Next, select the **Copilot** option.

   ![](../../media/database9.png)

2. Click on the **Get started** button.

   ![](../../media/database10.png)

3. Paste the following prompt in the **Copilot** chat box and click on **Send** button.

   ```
   Write me a query that will return the most sold product.
   ```

   <img alt="A picture of Copilot chat pane opened with written query above." src="../../media/Copilot/ChatPaneQuery.png" style="width:400px;">

4. Read the answer now and select the **Insert** button to input code into the Query Editor.

   >**Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

   <img alt="A picture of a demonstrating Copilot response and selecting insert query into the query editor." src="../../media/Copilot/InsertQuery.png" style="width:400px;">

5. Select the query that was inserted by **Copilot**, click on the **Run** icon and check the **Results**. 
   >**Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

   ![](../../media/Copilot3a.png)

### Task 2.2: Chat Pane: Get results from Copilot

1. Another way to use Copilot is to ask it to get results for you. Open the new query or clear the previous one to have a blank query editor. Paste the following question in the Copilot chat box and click on **Send** button
   ```
   What is the most sold product?
   ```

2. Observe that Copilot has returned the results in the Chat pane.

   >**Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

   <img alt="A picture of a demonstrating Copilot response stating what is the most sold product." src="../../media/Copilot/MostSoldProduct.png" style="width:400px;">


### Task 2.3: Chat Pane: Write (with approval)

1. Copilot is also able to write and execute queries on top of your database (with approval). You can choose which type of Copilot you want to use from the dropdown.

   <img alt="A picture of a choosing modes in Copilot." src="../../media/Copilot/WriteWithApproval.png" style="width:400px;">


2. Paste the following question in the **Copilot** chat box and click on **Send** button.
   ```
   Create a view in the SalesLT schema using this query and execute it.
   ```

3. Observe the Copilot's response and select **Run** to execute the given query on top of your database.

   >**Note:** Copilot responses may not match what is shown in the screenshot but will provide similar results.

   <img alt="A picture of a approving Copilot to execute a query." src="../../media/Copilot/ExecuteWithApproval.png" style="width:400px;">

4. Wait a few seconds while Copilot executes the query.

   ![Working on it / loading widget.](../../media/Copilot/WorkingOnIt.png)

9. In the **Explorer** pane on the left, expand the **SalesLT** schema. Open the **Views** folder, then select/click the view you just created. Review the displayed results to validate that the data matches your expectations.

   ![](../../media/copilot-7.png)


## What's next
Congratulations! You have learnt how to leverage **Copilot for SQL database in Microsoft Fabric** to enhance your **query-writing** experience. With these skills, you are now better equipped to write and execute SQL queries faster and troubleshoot errors effectively using Copilot. You are ready to move on to the next exercise: 
[Database development using VS Code](../Module%2003%20-%20Database%20Development%20using%20Visual%20Studio%20Code%20%26%20Github%20Copilot/Visual%20Studio%20Code%20integration%20with%20SQL%20database.md) to enhance your developer's productivity.


