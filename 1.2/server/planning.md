### Greek symbols are used for comprehensive purpose only.
### They hold no technical significance.
=====================================================================================
main routes :
- /load
- /search 
- /store
- /stats

=====================================================================================
defining RESTful API for '/load':
-------------------------------------------------------------------------------------
The task here is to  :
- accept columnar data (transaction dates, transaction amounts, 
    cheques info)
- create a dataframe of Entry type, let's call it φ
- map a HashTable, let's call it, Δ, out of φ
- send the following to be recorded as analytical matrices:
    - Number of sheets as α
    - Number of records in each sheet as n(α)
    - Size of HashTables created as δ(Δ)
    - Time taken to perform Hashing for each sheet as τ(n(α))
    - Memory occupied by each HashTable as μ(Δ)
    - Approximated time of O(n(α) log (n(α))) to compare the difference between our searching mechanisms
- return the current value of α after each load-up

======================================================================================
defining RESTful API for '/search':
--------------------------------------------------------------------------------------
the task here is to :
- accept job queue from frontend Q
- create a batch of jobs performing search 'n' match
- triggers search 'n' match on the batch of jobs
- use HashSearching mechanism for searching
- send the following to be recorded as analytical matrices :
    - Size of Job Queue, let's say n(Q)
    - Time taken to batch creation from Q, let's call it, τ(n(Q))
    - Time taken to perform search 'n' match(*) for each job in Q, 
        τ(*Q)
    - Number of records left in each sheet n(*Q(α))
- generate the BRS class instance
- write performance analytics to a file 'pa_records.txt'
- return an appropriate message for the search completion, or drop an error 

======================================================================================
defining RESTful API for '/store':
--------------------------------------------------------------------------------------
the task here is to :
- transform the leftover records from the pertaining HashTables into dataframes 
- write BRS class instance values to file
- write the respective dataframes to excel files 
- return appropriate message for the completion of write 
======================================================================================
defining RESTful API for '/stats': (for developers only)
--------------------------------------------------------------------------------------
- print the performance matrix (for developers only)
======================================================================================
FILE STRUCTURE :
--------------------------------------------------------------------------------------
server
├───controller  -> holds job-manager functionalities and re-routing capabilities
├───domain      -> holds concrete implementation classes of abstract-base classes in `services`
├───handlers    -> holds classes to handle the server APIs
├───pkg         -> holds server features like auto-upgrade, performance-benchamrking, etc
└───services    -> holds all the abstract-base classes and interfaces
======================================================================================
CLASSES TO USED:

-   DataFrame
-   HashTable
-   PerformanceMatrix
-   BRSStatement

-   DFToHashTableConverter
-   HashTableToDFConverter
-   JobSequencer
-   SearchNMatchTrigger

-   LoadRouteHandler
-   SearchRouteHandler
-   StatsRouteHandler
-   StoreRouteHandler
----------------------------------------------------------------------------------------
INTERFACES/ABCs TO USED:
-   RawObject
-   Matrix
-   Report
-   Converter
-   Handler
--------------------------------------------------------------------------------------------















