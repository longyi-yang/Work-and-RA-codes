setwd("D:/Personal/Desktop/文献/数据/Jilin_pm2.5_density")
library(stringr)
library(raster)
library(rasterVis)
library(ncdf4)
library(lattice)

nc_list = list.files(path = "D:/Personal/Desktop/文献/数据/Jilin_pm2.5_density",
           pattern = ".nc")

for (i in nc_list){
  
  ncfile = ncdf4::nc_open(i)
  ncname = names(ncfile$var)
  
  #Change the Input path.
  dir_i = str_glue("D:/Personal/Desktop/文献/数据/Jilin_pm2.5_density/{i}")
  input_nc = dir_i
  varname = ncname
  nc2raster = raster(input_nc,varname = varname,band = 1)
  
  #To output a quick view for the dataset
  png_name = str_glue("D:/Personal/Desktop/文献/数据/Jilin_pm2.5_density/{i}.png")
  png(png_name,
      height = 15,
      width = 20,
      units = 'cm',
      res = 1000)
  print(levelplot(nc2raster))
  dev.off()
  
  nc2raster = stack(input_nc,varname = varname)
  
  output_name = str_glue('D:/{i}.tif')
  output = output_name
  writeRaster(nc2raster,output,format = 'GTiff',overwrite = TRUE)
  #Change the output path to save Geotif data.
}

#(WGS84)

#预测
setwd("D:/Personal/Desktop/文献/数据")
library("forecast")
library("tseries")
library("readxl")

##Income
income_data <- read_excel("forR.xlsx",sheet = "income")
income_ts <- ts(income_data$income, frequency = 1, start = 1980)
#ADF
plot(income_ts)
income_ADF <- adf.test(income_ts)
income_ADF
#自动确定pf
income_arima <- auto.arima(income_ts)
accuracy(income_arima)
#                   ME     RMSE     MAE       MPE     MAPE      MASE      ACF1
#Training set 43.95446 224.5258 169.875 0.8776379 8.051728 0.3787728 -0.043359
#检验
qqnorm(income_arima$residuals)
qqline(income_arima$residuals)
Box.test(income_arima$residuals, type = "Ljung-Box")
#预测
income_forecast <- predict(income_arima, 9)
income_forecast
forecast(income_arima,9)
#Point Forecast    Lo 80    Hi 80    Lo 95    Hi 95
#2022       19081.67 18783.06 19380.27 18624.99 19538.34
#2023       20562.58 19974.88 21150.28 19663.77 21461.39
#2024       22030.93 21084.75 22977.10 20583.88 23477.97
#2025       23503.10 22149.21 24857.00 21432.50 25573.70
#2026       24974.11 23166.39 26781.83 22209.44 27738.78
#2027       26445.47 24142.69 28748.25 22923.68 29967.27
#2028       27916.73 25080.68 30752.78 23579.36 32254.09
#2029       29388.02 25983.08 32792.95 24180.62 34595.41
#2030       30859.29 26851.96 34866.63 24730.60 36987.99
plot(forecast(income_arima,9),
     main = "吉林农村人均年收入时间序列预测结果",
     ylab = "人均年收入(元)")

##population
population_data <- read_excel("forR.xlsx", sheet = "population")
population_ts <- ts(population_data$population, frequency = 1, start = 2005)
#ADF
plot(population_ts)
population_ADF <- adf.test(population_ts)
population_ADF
#自动确定pf
population_arima <- auto.arima(population_ts)
accuracy(population_arima)
#
#                  ME     RMSE     MAE          MPE      MAPE      MASE       ACF1
#Training set -6046.628 111053.3 81454.3 -0.006734826 0.7682413 0.3129389 0.01387455

#检验
qqnorm(population_arima$residuals)
qqline(population_arima$residuals)
Box.test(population_arima$residuals, type = "Ljung-Box")
#预测
forecast(population_arima,8)
plot(forecast(population_arima,8),
     main = "吉林农村人口时间序列预测结果",
     ylab = "人口数")
#forecast(population_arima,9)
#     Point Forecast   Lo 80   Hi 80   Lo 95    Hi 95
#2023        8328000 8177046 8478954 8097136  8558864
#2024        8140900 7803357 8478443 7624673  8657127
#2025        7953800 7388983 8518617 7089987  8817613
#2026        7766700 6939892 8593508 6502207  9031193
#2027        7579600 6460097 8699103 5867468  9291732
#2028        7392500 5952493 8832507 5190199  9594801
#2029        7205400 5419291 8991509 4473782  9937018
#2030        7018300 4862249 9174351 3720905 10315695


##home
home_data <- read_excel("forR.xlsx", sheet = "home")
home_ts <- ts(home_data$home, frequency = 1, start = 2003)
#ADF
plot(home_ts)
home_ADF <- adf.test(home_ts)
home_ADF
#自动确定pf
home_arima <- auto.arima(home_ts)
accuracy(home_arima)
#                    ME     RMSE      MAE        MPE      MAPE      MASE        ACF1
#Training set -6955.795 28622.83 20772.18 -0.1624882 0.5010444 0.6130501 -0.03359275
#检验
qqnorm(home_arima$residuals)
qqline(home_arima$residuals)
Box.test(home_arima$residuals, type = "Ljung-Box")
#Box-Ljung test
#data:  home_arima$residuals
#X-squared = 0.025014, df = 1, p-value = 0.8743

#预测
forecast(home_arima,9)
plot(forecast(home_arima,9),
     main = "吉林农村家庭户数时间序列预测结果",
     ylab = "户数")
#Point Forecast   Lo 80   Hi 80   Lo 95   Hi 95
#2022        4197806 4157833 4237779 4136672 4258939
#2023        4177811 4107514 4248109 4070301 4285322
#2024        4157817 4054525 4261109 3999846 4315788
#2025        4137823 3998475 4277170 3924710 4350936
#2026        4117828 3939434 4296223 3844997 4390659
#2027        4097834 3877544 4318124 3760930 4434738
#2028        4077840 3812954 4342725 3672733 4482946
#2029        4057845 3745801 4369890 3580614 4535076
#2030        4037851 3676205 4399497 3484761 4590940

##Death
death_data <- read_excel("forR.xlsx", sheet = "death")
death_ts <- ts(death_data$death, frequency = 1, start = 1997)
#ADF
plot(death_ts)
death_ADF <- adf.test(death_ts)
death_ADF
#自动确定pf
death_arima <- auto.arima(death_ts)
accuracy(death_arima)
#                       ME         RMSE          MAE     MPE     MAPE      MASE      ACF1
#Training set 0.0001393065 0.0004650668 0.0003309833 1.72291 5.393397 0.8885458 -0.108936
#检验
qqnorm(death_arima$residuals)
qqline(death_arima$residuals)
Box.test(death_arima$residuals, type = "Ljung-Box")
#预测
forecast(death_arima,9)
#     Point Forecast       Lo 80       Hi 80       Lo 95       Hi 95
#2022    0.007985232 0.007363852 0.008606612 0.007034913 0.008935551
#2023    0.008018495 0.007277719 0.008759271 0.006885576 0.009151414
#2024    0.008006820 0.007124217 0.008889423 0.006656996 0.009356644
#2025    0.008010918 0.007018868 0.009002968 0.006493708 0.009528127
#2026    0.008009479 0.006914961 0.009103998 0.006335558 0.009683401
#2027    0.008009984 0.006823085 0.009196883 0.006194779 0.009825190
#2028    0.008009807 0.006736797 0.009282817 0.006062906 0.009956708
#2029    0.008009869 0.006656353 0.009363385 0.005939845 0.010079894
#2030    0.008009847 0.006580306 0.009439389 0.005823553 0.010196142

plot(forecast(death_arima,9),
     main = "吉林农村死亡率时间序列预测结果",
     ylab = "死亡率")

#自动的效果不好，改为手动
ndiffs(death_ts) #n=1
n_death_ts <- diff(death_ts,1)
death_1_ADF <- adf.test(n_death_ts)
death_1_ADF
Box.test(n_death_ts,type = "Ljung-Box") #p<0.05,not white noise
#acf and pacf
acf(n_death_ts, main = 'n_acf') 
pacf(n_death_ts, main = 'n_pacf') 
#p=0, d= , q= 
death_arima_manual <- arima(death_ts,
                            order = c(0,1,1))
accuracy(death_arima_manual)
forecast(death_arima_manual,9)
plot(forecast(death_arima,9),
     main = "吉林死亡率时间序列预测结果",
     ylab = "死亡率")

#家庭户数，人口和用电量之间的相关性检验
##用电
power_data <- read_excel("forR.xlsx",sheet = "power")

##Pearson检验
cor.test(home_data$home[1:18],power_data$usage,method=c("pearson"))
cor.test(population_data$population[1:18],power_data$usage,method=c("pearson"))
#Pearson's product-moment correlation

#data:  home_data$home[1:18] and power_data$usage
#t = 16.868, df = 16, p-value = 1.299e-11
#alternative hypothesis: true correlation is not equal to 0
#95 percent confidence interval:
# 0.9274670 0.9901075
#sample estimates:
#      cor 
#0.9730151 

#Pearson's product-moment correlation

#data:  population_data$population[1:18] and power_data$usage
#t = -9.6923, df = 16, p-value = 4.236e-08
#alternative hypothesis: true correlation is not equal to 0
#95 percent confidence interval:
# -0.9718358 -0.8048432
#sample estimates:
#       cor 
#-0.9243733 


#做线性回归
model_ph <- lm(power_data$usage~home_data$home[1:18])
summary(model_ph)
#Residuals:
#  Min     1Q Median     3Q    Max 
#-46821 -15918   1260  17068  48128 

#Coefficients:
#                        Estimate Std. Error t value Pr(>|t|)    
#(Intercept)          -2.044e+06  1.462e+05  -13.98 2.18e-10 ***
#  home_data$home[1:18]  6.001e-01  3.558e-02   16.87 1.30e-11 ***
#  ---
#  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

#Residual standard error: 26430 on 16 degrees of freedom
#Multiple R-squared:  0.9468,	Adjusted R-squared:  0.9434 
#F-statistic: 284.5 on 1 and 16 DF,  p-value: 1.299e-11

model_pp <- lm(power_data$usage~population_data$population[1:18])
summary(model_pp)

#基于home的预测结果，对用电量做线性估计
usage_predict_x <- forecast(home_arima,9)$mean
home_df <- as.data.frame(usage_predict_x)
colnames(home_df)<-"home"
home_df_manual <- data.frame(
  home = c(4197806,4177811,415817,4137823,4117828,4097834,4077840,4057845,4037851)
  )
model_ph_predict <- predict(model_ph,newdata=home_df,
                            se.fit = FALSE,
                            interval = "confidence"
                            )
model_ph_predict
