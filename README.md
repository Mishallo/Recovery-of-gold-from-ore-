# Recovery-of-gold-from-ore-
Prepare a prototype of the machine learning model for the "Figure". The company develops solutions for the efficient operation of industrial enterprises.  The model should predict the recovery rate of gold from gold-bearing ore. Use data with extraction and purification parameters.  
The data is in three files:  
gold_industry_train.csv — training sample;  
gold_industry_test.csv — test sample;  
gold_industry_full.csv — source data.  
The data is indexed by the date and time the information was received (the date attribute). The time-adjacent parameters are often similar.  
Some parameters are not available because they are measured and/or calculated much later. Because of this, the test sample lacks some of the features that may be in the training sample. There are also no target features in the test set.  
The source dataset contains training and test samples with all the features.  
You have the raw data at your disposal: they were just unloaded from the storage. Before starting to build a model, check them for correctness according to our instructions.  
Instructions for the implementation of the project  
1. Prepare the data  
1.1. Open the files and examine them.  
File path:  
/datasets/gold_industry_train.csv.[ Download dataset](https://code.s3.yandex.net/datasets/gold_industry_train.csv)  
/datasets/gold_industry_test.csv. [Download dataset](https://code.s3.yandex.net/datasets/gold_industry_test.csv)  
/datasets/gold_industry_full.csv. [Download the dataset ](https://code.s3.yandex.net/datasets/gold_industry_full.csv)   
1.2. Check that the enrichment efficiency is calculated correctly. Calculate it on the training sample for the rougher.output.recovery attribute. Find the MAE between your calculations and the attribute value. Describe the conclusions.  
1.3. Analyze the features that are not available in the test sample. What are these parameters? What type do they belong to?  
1.4. Perform data preprocessing.  
2. Analyze the data  
2.1. Look at how the concentration of metals (Au, Ag, Pb) changes at various stages: in the raw material, in the rough concentrate, in the concentrate after the first purification and in the final concentrate. What features do distributions have? Describe the conclusions.  
2.2. Compare the size distributions of the feedstock granules in the training and test samples. If the distributions are very different from each other, the model estimate will be incorrect.  
2.3. Examine the total concentration of metals at different stages: in the raw material, in the rough concentrate, in the concentrate after the first purification and in the final concentrate.  
3. Build a model  
3.1. Write a function to calculate the final sMAPE.  
3.2. Train different models and evaluate their quality by cross-validation. Choose the best model and test it on a test sample. Describe the conclusions.
The formulas of quality metrics will be useful to you:
the sMAPE formula the
![image](https://github.com/Mishallo/Recovery-of-gold-from-ore-/assets/167329415/d2336b23-6c79-4118-8243-2b0aaa189aa9)
formula of the final sMAPE
![image](https://github.com/Mishallo/Recovery-of-gold-from-ore-/assets/167329415/315fa97b-d17a-449f-b3b3-366b7393af42)
