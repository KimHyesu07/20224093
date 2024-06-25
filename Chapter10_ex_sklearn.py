Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import pandas as pd
... import matplotlib.pyplot as plt
... from sklearn.model_selection import train_test_split
... from sklearn.linear_model import LinearRegression
... from sklearn.metrics import mean_squared_error, r2_score
... 
... """데이터 생성 (예제 데이터셋)"""
... np.random.seed(0)
... X = 2 * np.random.rand(100, 1)
... y = 4 + 3 * X + np.random.randn(100, 1)
... 
... """데이터를 훈련 세트와 테스트 세트로 나누기"""
... X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
... 
... """모델 생성"""
... regressor = LinearRegression()
... 
... """모델 훈련"""
... regressor.fit(X_train, y_train)
... 
... """예측"""
... y_pred = regressor.predict(X_test)
... 
... """결과 출력"""
... print(f'회귀 계수: {regressor.coef_}')
... print(f'절편: {regressor.intercept_}')
... print(f'평균 제곱 오차 (MSE): {mean_squared_error(y_test, y_pred)}')
... print(f'결정 계수 (R^2 점수): {r2_score(y_test, y_pred)}')
... 
... """시각화"""
... plt.scatter(X_test, y_test, color='blue', label='Actual')
... plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
... plt.title('Actual vs Predicted')
... plt.xlabel('X')
... plt.ylabel('y')
plt.legend()
plt.show()
