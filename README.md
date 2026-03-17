![](https://raw.githubusercontent.com/microsoft/sqlworkshops/master/graphics/microsoftlogo.png)
# Workshop: Build AI-Ready applications with SQL Database in Microsoft Fabric

## Overview

#### A Microsoft Workshop from the SQL Server Team

Welcome to the *SQL database in Microsoft Fabric* workshop. This workshop is designed to provide you with a comprehensive understanding of SQL database in Microsoft Fabric and its integration with other services. Throughout this workshop, you will learn how to create, manage, and optimize SQL databases, as well as how to leverage artificial intelligence and build applications using GraphQL API builder.


## Introduction to SQL Database in Fabric

### Understanding SQL Database in Fabric

**SQL database** in Microsoft Fabric is a developer-friendly transactional database, based on **Azure SQL Database**, that allows you to easily create your operational database in Microsoft Fabric. A SQL database in Microsoft Fabric uses the same SQL Database Engine as Azure SQL Database.

SQL database in Fabric is:

- The home in Fabric for OLTP workloads
- Easy to configure and manage
- Set up for analytics by automatically replicating the data into OneLake in near real time
- Integrated with development frameworks and analytics
- Based on the underlying technology of **Mirroring in Fabric**
- Queried in all the same ways as **Azure SQL Database**, plus a **web-based editor in the Fabric portal**

### Key Benefits of Using SQL Database in Fabric
SQL database in Microsoft Fabric is a developer-friendly transactional database based on the Azure SQL Database engine. It is simple, autonomous, secure by default, and AI-integrated. Being part of Microsoft Fabric, it benefits from Fabric's promises and offers tight integration with other workloads within Microsoft Fabric.

![](media/f1.png)

With your SQL database in Fabric, you can easily build OLTP applications while minimizing the need to stitch together multiple services to create an end-to-end solution.

When you provision a SQL database, the data is stored in MDF and LDF formats. The data is then automatically replicated into OneLake and converted to Parquet, in an analytics-ready format. This enables downstream scenarios like Data Engineering, Data Science, and more.


#### Sharing
 
Sharing enables ease of access control and management, while security controls like row-level security (RLS), object-level security (OLS) and more make sure you can control access to sensitive information. Sharing also enables secure and democratized decision-making across your organization.
 
By sharing your SQL database, you can grant other users or a group of users, access to a database without giving access to the workspace and the rest of its items. When someone shares a database, they also grant access to the SQL analytics endpoint and associated default semantic model.
 
#### Connect
 
Like other Microsoft Fabric item types, SQL databases rely on Microsoft Entra authentication.
To successfully authenticate to a SQL database, a Microsoft Entra user, a service principal, or their group, must have the Read item permission to the SQL database in Fabric.
 
![](media/04.png)

In addition to the Fabric SQL database Query Editor, you can also connect your Fabric SQL database to your preferred client tools, including SQL Server Management Studio and the mssql extension with Visual Studio Code. 
 
#### Cross-database queries
 
With the data from your SQL database automatically stored in OneLake, you can write cross-database queries, joining data from other SQL databases, mirrored databases, warehouses, and the SQL analytics endpoint in a single T-SQL query. All this is currently possible with queries on the SQL analytics endpoint of the SQL database, or lakehouse.
 
#### Data Engineering with your SQL database in Fabric
 
Microsoft Fabric provides various data engineering capabilities to ensure that your data is easily accessible, well-organized, and high-quality. With Microsoft Fabric Data Engineering, you can:
 
- Create and manage your data as Spark using a SQL database in Fabric.
- Design pipelines to copy data into your SQL database in Fabric.
- Use Spark job definitions to submit batch/streaming jobs to Spark cluster.
- Use notebooks to write code for data preparation and transformation.
 
#### Data Science with your SQL database in Fabric
 
Data Science in Microsoft Fabric empowers users to complete end-to-end data science workflows for the purpose of data enrichment and business insights. You can complete a wide range of activities across the entire data science process, all the way from data exploration, preparation and cleansing to experimentation, modeling, model scoring and serving of predictive insights to BI reports.
 
#### Database portability and deployments with SqlPackage
 
SqlPackage is a cross-platform command line tool that enables database interactions that move entire databases or database objects. The portability (import/export) of a database managed in Azure or in `Fabric ensures that your data is portable should you want to migrate later on. The same portability also enables certain migration scenarios through self-contained database copies (.bacpac) with import/export operations.
 
SqlPackage can enable easy database deployments of incremental changes to database objects (new columns in tables, alterations to existing stored procedures, etc.). SqlPackage can extract a .dacpac file containing the definitions of objects in a database, and publish a .dacpac file to apply that object state to a new or existing database. The publish operation also integrates with SQL projects, which enables offline and more dynamic development cycles for SQL databases.
 
#### Integration with Fabric source control
SQL database is integrated with [Fabric continuous integration/continuous development](https://learn.microsoft.com/fabric/cicd/cicd-overview). You can use the built-in git repository to manage your SQL database.
 
#### Create GraphQL API from Fabric portal
 
You can use the Microsoft Fabric portal to easily [create a GraphQL API](https://learn.microsoft.com/fabric/database/sql/graphql-api) for your SQL database.
 
#### Capacity management
 
You can use the [Microsoft Fabric Capacity Metrics app](https://learn.microsoft.com/fabric/enterprise/metrics-app) to monitor the SQL database usage and consumption in non-trial Fabric capacities.
 
#### Mirroring for Azure SQL Database
 
Do you already have an external database and want to leverage Fabric's integration? You can use Mirroring in Fabric as a low-cost and low-latency solution to bring data from various systems together. You can continuously replicate your existing data estate directly into Fabric's OneLake, including data from an existing [Azure SQL Database](https://learn.microsoft.com/fabric/database/mirrored-database/azure-sql-database).


## Workshop Content
The workshop is divided into several modules, each focusing on a specific aspect of SQL database in Microsoft Fabric. By the end of this workshop, you will have gained practical knowledge and hands-on experience in the following areas:

### 0. [Pre-Requisites](/sqldev/Module%2000%20-%20Pre-Requisites/00%20-%20Pre-Requisites.md)

In this module, you will set up the necessary components and configurations required for the workshop. This includes setting up a PowerBI account, enabling Microsoft Fabric Tenant settings, and creating a Microsoft Azure account.

### 1. [Introduction to SQL database in Fabric](/sqldev/Module%2001%20-%20Introduction%20to%20SQL%20database%20in%20Fabric/01%20-%20Getting%20Started.md)

In this module covers the basics of getting started with SQL database in Fabric. You will learn how to create a database, and seed the database with initial data that will be used in later modules.

### 2. [Explore AI and Copilot capabilities](/sqldev/Module%2002%20-%20Explore%20AI%20and%20Copilot%20capabilities/Copilot%20capabilities%20for%20SQL%20database%20in%20Microsoft%20Fabric.md)

In this module covers how to use Copilot in Fabric SQL for faster query development through inline suggestions, natural-language-to-SQL generation, query explanations, and automatic error fixes.

### 3. [Database Development using Visual Studio Code & Github Copilot](/sqldev/Module%2003%20-%20Database%20Development%20using%20Visual%20Studio%20Code%20%26%20Github%20Copilot/Visual%20Studio%20Code%20integration%20with%20SQL%20database.md)

In this module you will learn how to use Visual Studio Code & Github copilot to seamlessly connect and work with your SQL database in Fabric.

### 4. [Get your database AI ready using Vector & RAG patterns](/sqldev/Module%2004%20-%20Get%20your%20database%20AI%20ready%20using%20Vector%20%26%20RAG%20patterns/Prepare%20your%20data%20to%20store%20Vector%20data%20for%20Vector%20search%20to%20enavle%20AI%20application%20development.md)

In this module you will learn how to implement Retrieval-Augmented Generation (RAG) using Azure OpenAI and vector-based search. RAG is a powerful architecture that enhances the capabilities of large language models by grounding their responses in external knowledge sources.


### 5. [Create GraphQL API for Chatbot Application](/sqldev/Module%2005%20-%20Create%20GraphQL%20API%20for%20Chatbot%20Application/Create%20GraphQL%20API%20for%20RAG%20Application.md)

In this module you will learn and create GraphQL API in Fabric to use in your chatbot application

### 6. [Build a Chatbot Application With VS Code & github copilot](/sqldev/Module%2006%20-%20Build%20a%20Chatbot%20Application%20With%20VS%20Code%20%26%20github%20copilot/Build%20a%20Chatbot%20Application%20With%20GHCP%20%2B%20VSCode.md)

In this module, you will learn how to create a chatbot using Visual Studio code and Github copilot using prompts. You will use the graphQL API created in module 5.

### 7. [Integrate with Data Agents, Data Virtualization & Power BI](/sqldev/Module%2007%20-%20Integrate%20with%20%20Data%20Agents%2C%20Data%20Virtualization%20%26%20Power%20BI/01%20-%20Data%20Agent.md)

In this module, you will learn about three integration patterns: governed Data Agent Q&A, OneLake data virtualization via OPENROWSET/external tables, and Copilot-assisted Power BI reporting.


### 8. [Reporting with action using Translytical Taskflows in Power BI](sqldev/Module 08 - Reporting with action using Translytical Taskflows in Power BI/01 - Data population.md)

In this exercise you will build on the examples from the previous exercise to **score for sentiment** user reviews of products for AdventureWorks.  You will then use Translytical Taskflows to create a **user data function**,**embed it within a Power BI report**, and **respond to the reviews** in order to determine if any actions or follow up is needed by you, the AdventureWorks employee, who owns the product.


### 9. [Source control integration with Github](/sqldev/Module%2009%20-%20Source%20control%20integration%20with%20Github/Github%20Source%20Control.md)

In this module, you will learn about managing the lifecycle of your application using source control. You will also learn how to monitor and maintain your SQL database in Fabric, including setting up Git integration, linking GitHub repositories to Azure DevOps, and synchronizing your workspace with the Git branch.


### 10. [Performance Dashboard](/sqldev/Module%2010%20-%20Performance%20Dashboard/Monitor%20your%20SQL%20database.md)
 
In this exercise, you will learn to monitor SQL database performance and CU usage.
## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Legal Notices

### License
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see [the LICENSE file](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web/blob/master/LICENSE), and grant you a license to any code in the repository under [the MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE file](https://github.com/MicrosoftDocs/mslearn-tailspin-spacegame-web/blob/master/LICENSE-CODE).

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

---
