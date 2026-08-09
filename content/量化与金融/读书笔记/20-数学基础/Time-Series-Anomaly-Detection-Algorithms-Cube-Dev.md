---
title: Time Series Anomaly Detection Algorithms - Cube Dev
source: converted:attachments/documents/Anomaly-Detection-5504b7dfdf94/Time Series
  Anomaly Detection Algorithms - Cube Dev.pdf
source_type: PDF
quality: draft
attachments:
- file: attachments/documents/Anomaly-Detection-5504b7dfdf94/Time Series Anomaly Detection
    Algorithms - Cube Dev.pdf
  title: Time Series Anomaly Detection Algorithms - Cube Dev.pdf
custom-width: 85
---

# Time Series Anomaly Detection Algorithms - Cube Dev

S - 

Announcing cube.js Open Source Analytics Framework 

At Statsbot, we’re constantly reviewing the landscape of anomaly detection approaches and re:nishing our models based on this research. 

This article is an overview of the most popular anomaly detection algorithms for time series and their pros and cons. 

This post is dedicated to non-experienced readers who just want to get a sense of the current state of anomaly detection techniques. Not wanting to scare you with mathematical models, we hid all the math under referral links. 

# Important Types of Anomalies 

<mark>Anomaly detection problem for time series is usually formulated as !nding outlier data points relative to some standard or usual signal</mark> . While there are plenty of anomaly types, we’ll focus only on the most important ones from a business perspective, such as unexpected spikes, drops, trend changes and level shifts. 

Imagine you track users at your website and see an unexpected growth of users in a short period of time that looks like a spike. These types of anomalies are usually called additive outliers. 

time 

instead of the original one. 

### Cons 

The cons of this approach are in its rigidity regarding tweaking options. All you can tweak is your con:dence interval using the signi:cance level. 

The typical scenario in which is doesn’t work well is when characteristics of your signal have changed dramatically. For example, you’re tracking users on your website that was closed to the public, and then was suddenly opened. In this case, you should track anomalies that occur before and after launch periods separately. 

# Classi8cation and Regression Trees 

Classi:cation and regression trees is one of the most robust and most eOective machine learning techniques. It may also be applied to anomaly detection problems in several ways. 

- First, you can use supervised learning to teach trees to classify anomaly and non-anomaly data points. In order to do that you’d need to have labeled anomaly data points. 

- The second approach is to use unsupervised learning to teach CART to predict the next data point in your series 

learning and get sophisticated models. 

### Cons 

The weakness is a growing number of features can start to impact your computational performance fairly quickly. In this case, you should select features consciously. 

# ARIMA 

ARIMA is a very simple method by design, but still powerful enough to forecast signals and to :nd anomalies in it. 

It’s based on an approach that several points from the past generate a forecast of the next point with the addition of some random variable, which is usually white noise. As you can imagine, forecasted points in the future will generate new points and so on. Its obvious eOect on the forecast horizon: the signal gets smoother. 

The diUcult part in appliance of this method is that you should select the number of diOerences, number of autoregressions, and forecast error coeUcients. 

Each time you work with a new signal 

The favored implementation of this approach is tsoutliers R package. It’s suitable to detect all types of anomalies in the case that you can :nd a suitable ARIMA model for your signal. 

# Exponential Smoothing 

Exponential smoothing techniques are very similar to the ARIMA approach. The basic exponential model is equivalent to the ARIMA (0, 1, 1) model. 

The most interesting method from the anomaly detection perspective is Holt-Winters seasonal method. You should de:ne your seasonal period which can equal to a week, month, year, etc. 

In the case you need to track several seasonal periods, such as having both week and year dependencies, you should select only one. Usually, it’ll be the shortest one: a week in this example. 

This is clearly a drawback of this approach, which aOects the forecasting horizon a lot. 

Anomaly detection can be done using the same statistical tests for an outlier, as in the case of STL or CARTs. 

# Neural Networks 

As in the case of CART, you have two ways to apply neural networks: supervised and unsupervised learning. 

As we’re working with time series, the most suitable type of neural network is LSTM. This type of Recurrent Neural Network, if properly built, will allow you to model the most sophisticated dependencies in your time series as well as advanced seasonality dependencies. 

This approach can also be very helpful if you have multiple time series coupled with each other. 

This area is still on-going research, and it requires a lot of work to build the model for your time series. Should you succeed, you may achieve outstanding performance results in terms of accuracy. 

# To Keep in Mind 

1. Try the simplest model and algorithm that :t your problem the best. 

2. Switch to more advanced techniques if it doesn’t work out. 

3. Starting with more general solutions that cover all the cases is a tempting option, but it’s not always the best. 

At Statsbot, to detect anomalies at scale we use diOerent 

combinations of techniques starting with STL and ending with CART and LSTM models. 

Was it helpful? Please recommend and share this article to help other people And it. 

## **Enjoyed the article?** 

# YOU’D ALSO LIKE:

---

## 源文件

- [[Time Series Anomaly Detection Algorithms - Cube Dev.pdf]]