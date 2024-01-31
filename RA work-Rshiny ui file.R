library(shiny)
library(shinydashboard)
library(mapdeck)
library(colourvalues)
library(tidyverse)
library(ggplot2)
library(googleVis)
library(colourvalues)
library(jsonify)
library(geojsonsf)
library(spatialwidget)
library(googlePolylines)


### add choices bar's content
#for states
choices_impact <- c("Deaths due to ozone exposure", "Deaths due to PM2.5 exposure", "Deaths due to heat exposure", 
                    "Respiratory hospital admission", 
                    "Bronchitis in children ages 6-12", 
                    "Work lost days, ages 15-64","Yield loss of wheat", "Yield loss of rice","Yield loss of maize",
                    "Yield loss of soybeans",
                    "Economic loss of respiratory hospital admissions", "Economic loss of work lost days, age 15-64",
                    "Economic loss of wheat yield loss","Economic loss of rice yield loss",
                    "Economic loss of maize yield loss","Economic loss of soybean yield loss",
                    "Asthma emergency room visits, all age",
                    "Cardiovascular hospital admission, <65",
                    "Cardiovascular hospital admission, >65",
                    "Adult asthma hospital admission",
                    "Child asthma hospital admission",
                    "Labor loss due to high temperature"
)
choices_year <- unique(testoriginal$Years)
choices_ssp <- c("SSP1-1.9","SSP1-2.6","SSP2-4.5","SSP3-7.0LOW","SSP4-3.4","SSP4-6.0","SSP5-3.4","SSP19","SSP19US")

#for city
choices_impact_city <- c("Deaths due to ozone exposure", "Deaths due to PM2.5 exposure", "Deaths due to heat exposure", 
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


shinyUI(dashboardPage(skin='green',
                      dashboardHeader(
                        title = "Health, Climate and Economic Effects of Decarbonization",
                        titleWidth = 800
                      ),
                      dashboardSidebar(width = 300,
                                       sidebarMenu(
                                         menuItem("Introduction", tabName = "intro", icon = icon('align-justify')),
                                         menuItem("State-Level Results", tabName = "states", icon = icon('map')),
                                         menuItem("City-Level Results", tabName = "cities", icon = icon('map'))
                                       )),
                      dashboardBody(
                        tabItems(
                          tabItem(tabName = "intro",
                                  HTML(
                                    "<h2>Health, Climate and Economic Effects of US and Global Decarbonization</h2> 
                <p>State-level results for the US are provided here.</p>
                
                <p>Results shown here are based upon...</p>"),
                                  width = 12),
                          tabItem(tabName = "states", 
                                  h3(strong("Select Impact, Year and SSP option")),
                                  fluidRow(
                                    box(column(selectInput("ssp_option", "Choose SSP", choices_ssp, selected="SSP1-1.9"),
                                               width=3),
                                        column(selectInput("year_option", "Choose year", choices_year, selected="2070"),
                                               width=3),
                                        column(selectInput("impact_option","Choose Impact",choices_impact,selected = "Deaths due to ozone exposure"),
                                               width=6)                                    
                                  )
                                  ),
                #responses
                                  fluidRow(
                                    tags$style("#mapheadingtext{font-size:30px}"),
                                    box(column(8,strong(uiOutput("mapheadingtext")),
                                        htmlOutput("testmap")),
                                        column(4,valueBoxOutput("total_value", width = '100%')),
                                    width=12)

                        )
                      ),
                tabItem(tabName = "cities", 
                        h3(strong("Select Impact, Year and SSP option")),
                        fluidRow(
                          box(column(selectInput("ssp_option", "Choose SSP", choices_ssp, selected="SSP1-1.9"),
                                     width=3),
                              column(selectInput("year_option", "Choose year", choices_year, selected="2070"),
                                     width=3),
                              column(selectInput("impact_option","Choose Impact",choices_impact_city,selected = "Deaths due to ozone exposure"),
                                     width=6)                                    
                          )
                        ),
                        #responses
                        fluidRow(
                          tags$style("#mapheadingtext{font-size:30px}"),
                          box(column(12,strong(uiOutput("mapheadingtext_city")),
                                     htmlOutput("testmap_city")),
                          )              
                )))

)
)
)

