![](https://raw.githubusercontent.com/microsoft/sqlworkshops/master/graphics/microsoftlogo.png)

# Pre-Requisites

This workshop covering *SQL database in Microsoft Fabric* requires all attendees to bring their own device and establish an internet connection. 

*Note: All prerequisite activities must be completed prior to class - there will not be time to perform these operations during the workshop.*

## Pre-deployed components for the workshop:
- **PowerBI Account**: *[Power BI Sign in](https://app.powerbi.com/singleSignOn?ru=https%3A%2F%2Fapp.powerbi.com%2F%3FnoSignUpCheck%3D1)*. You will need a PowerBI account with existing Fabric capacity.
- **Enable Microsoft Fabric Tenant Settings**: *[Instructions to enable Microsoft Fabric  for your organizatio](https://learn.microsoft.com/fabric/admin/fabric-switch).*
- **Microsoft Azure Account**: This workshop uses the *[Microsoft Azure](https://ms.portal.azure.com/#home)* platform to host the Azure OpenAI model you will use.
    - You will need to have the **gpt-4-1** and **text-embeddings-ada-002** models deployed.

*Note: You don't have to perform these steps, you will just use it during the workshop. But, if you intend to come back to the workshop on your own time, you'll need to do the steps above.*

## [Action required] Environment configuration by the workshop participants:
- **Git source control repository**: You will need an account and an empty git repository in [GitHub](https://github.com/). If you don't have an account, you can create a free account through [https://github.com/join](https://github.com/join).

## Technical Knowledge
Good understanding of relational database, app dev and data & analytics platform concepts
- Hands on experience writing **T SQL** queries, including:
   - SELECT statements, **JOINs**, Basic aggregations
   - Familiarity with **SQL Server architecture** (databases, tables etc)
- Build apps using **Visual Studio Code**
- Familiarity with data and analytics concepts, such as datasets and reporting

## Tools & Software
1)	Bring your own laptop. Windows PC preferred as Power BI Desktop only works on Windows OS with Edge as a modern web browser 
2)	You will need a Github account and an empty git repository in GitHub. If you don't have an account, you can create a free account through https://github.com/join
3)	Install *[Visual Studio Code](https://code.visualstudio.com/)* & Python Programming Language
    - Install *[MSSQL extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql)*
    - Install *[Fabric extension for VS Code](https://marketplace.visualstudio.com/items?itemName=fabric.vscode-fabric)*
    - Install *[Python 3.14.2](https://www.python.org/downloads/release/python-3142/)*






4) Enabling **Translytical Task Flows** in Power BI Desktop
   - Download and Open Power BI Desktop 
   - If not already installed, download it from the official site: https://powerbi.microsoft.com/desktop/.
   - Launch **Power BI Desktop** once installation is complete.
   - From the top menu bar, click on **File**.

    ![](../../media/gr30.png)
    
   - Select **Options and Settings** → **Options**.

    ![](../../media/gr31.png)

   - In the Options window, go to **Preview features**.
   - Enable **Translytical task flow** by checking the box.

    ![](../../media/gr32.png)

   - Restart Power BI Desktop to apply the changes.

<!-- 
## Optional configuration:
- **VS Code**: Install *[Visual Studio Code](https://code.visualstudio.com/)* and the [SQL Database Projects extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.sql-database-projects-vscode).

  -->

*Note: Only if you want to follow the proctor during the workshop itself or after the workshop to follow through the demos configure components from this section.*

---

## FAQs
[FAQs for SQL DB in Fabric Hands-On Workshop](https://github.com/sukkaur/SQLConSQLdbinFabricWorkshop/blob/main/sqldev/Module%2000%20-%20Pre-Requisites/FAQs.md)

---

Next, continue to [**Introduction and Getting Started**.](../Module%2001%20-%20Introduction%20to%20SQL%20database%20in%20Fabric/01%20-%20Getting%20Started.md)


