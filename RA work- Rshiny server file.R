
setwd("C:/Users/longyiyang/Desktop/ra/shiny")
###load data
##states_impacts(from prof drew)
states_Impacts <- read.csv("impactsSSP_for_shinyapp.csv")
states_Impacts <- states_Impacts %>% filter(State.Name != "U.S. total") #what does this do? #I think it removes "us total" from the column

###test
#for state data
testoriginal<-read.csv("test.csv")
test<-testoriginal%>%filter(States !="U.S. total")
testtotal<-subset(testoriginal,States =="U.S. total")
naming_dataset<-read.csv("names.csv")
#for city data
testcityoriginal<-read.csv("testcity.csv")
naming_dataset_city<-read.csv("names_city.csv")


###descriptors###
impact_descriptorsL <- c("Deaths due to ozone exposure", 
                         "Deaths due to PM2.5 exposure", 
                         "Deaths due to heat exposure", 
                         "Respiratory hospital admission", 
                         "Bronchitis in children ages 6-12", 
                         "Work lost days, ages 15-64",
                         "Yield loss of wheat", 
                         "Yield loss of rice",
                         "Yield loss of maize",
                         "Yield loss of soybeans",
                         "Economic loss of respiratory hospital admissions", 
                         "Economic loss of work lost days, age 15-64",
                         "Economic loss of wheat yield loss",
                         "Economic loss of rice yield loss",
                         "Economic loss of maize yield loss",
                         "Economic loss of soybean yield loss",
                         "Asthma emergency room visits, all age",
                         "Cardiovascular hospital admission, <65",
                         "Cardiovascular hospital admission, >65",
                         "Adult asthma hospital admission",
                         "Child asthma hospital admission",
                         "Labor loss due to high temperature"
)

impact_descriptorsL_city <- c("Deaths due to ozone exposure", "Deaths due to PM2.5 exposure", "Deaths due to heat exposure", 
                              "Respiratory hospital admission", 
                              "Bronchitis in children ages 6-12", 
                              "Work lost days, ages 15-64",
                              "Economic loss of respiratory hospital admissions", "Economic loss of work lost days, age 15-64",
                              "Asthma emergency room visits, all age",
                              "Cardiovascular hospital admission, <65",
                              "Cardiovascular hospital admission, >65",
                              "Adult asthma hospital admission",
                              "Child asthma hospital admission",
                              "Labor loss due to high temperature"
)

###for "Ozone exposure" and "PM2.5 exposure", it seems that my csv file does not have these two value.

shinyServer(function(input, output){
  ###test###
  #states
  testoutFrame <- test %>% dplyr::select(States, Years, SSPs, Impacts, Value)
  testoriginaloutFrame <- testoriginal %>% dplyr::select(States, Years, SSPs, Impacts, Value)
  testtotaloutFrame<- testtotal %>% dplyr::select(States, Years, SSPs, Impacts, Value)
  #cities
  testoriginaloutFrame_city <- testcityoriginal %>% dplyr::select(States, Years, SSPs, Impacts, Value)
 
  
  

  ###output###
  #states
  test_group <- reactive({
    testoutFrame %>% 
      filter(Years == input$year_option & SSPs == input$ssp_option & Impacts == input$impact_option)
  })
  #cities
  test_group_city <- reactive({
    testoriginaloutFrame_city %>% 
      filter(Years == input$year_option & SSPs == input$ssp_option & Impacts == input$impact_option)
  })
  
  ###textoutput###
  #states
  LegendNum <- reactive({
    naming_dataset_city %>% filter(Impact_Group == input$impact_option) %>% pull(Value)
  })
  output$mapheadingtext<-renderUI({
    as.character(impact_descriptorsL[LegendNum()])})
  #cities
  LegendNum_city <- reactive({
    naming_dataset %>% filter(Impact_Group == input$impact_option) %>% pull(Value)
  })
  output$mapheadingtext_city<-renderUI({
    as.character(impact_descriptorsL_city[LegendNum_city()])})  
  
  ###valuebox output###
  #states
  output$total_value <- renderValueBox({
    valueBox(
      testtotaloutFrame %>% filter(Years == input$year_option & SSPs == input$ssp_option & Impacts == input$impact_option)
      %>% dplyr::select(Value),
      "Total Amount in US",     
      #icon = icon("angle-double-down"),
      icon = icon("arrow-circle-down"),
      color = 'green',
      width=12)
    })
  
  ###
  
  output$sample<- renderGvis({
    gvisGeoChart(ssp119, "States", "O3_deaths_per_yr_2070",
                 options=list(region="US", displayMode="regions",
                              resolution="provinces",
                              width="1000", height="800"))
  })
  output$testmap<- renderGvis({
      gvisGeoChart(na.omit(test_group()), "States","Value",
                   options=list(region="US", displayMode="regions",
                                resolution="provinces",
                                colorAxis="{colors:['green', 'white']}",
                                datalessRegionColor="gray",
                                width="1000", height="800"))
  })
  output$testmap_city<- renderGvis({
      gvisGeoChart(na.omit(test_group_city()), "States","Value",
                   options=list(region="US", displayMode="markers",
                                resolution="cities",
                                colorAxis="{colors:['green', 'white']}",
                                datalessRegionColor="gray",
                                width="1000", height="800"))  
    # using width="auto" and height="auto" to
    # automatically adjust the map size
  })  
  
})
