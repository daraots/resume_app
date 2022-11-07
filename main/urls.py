from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('Portfolio/', views.ContactView.as_view(), name="Portfolio"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('student-enrollment-dashboards/', views.StudentEnrollmentDashboardsView.as_view(), name="student-enrollment-dashboards"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('about/', views.AboutView.as_view(), name="about"),
	path('typing/', views.TypingView.as_view(), name="typing"),
	path('world-trade-statistics/', views.WorldTradeStatisticsView.as_view(), name="world-trade-statistics"),
	path('student-feedback-survey/', views.StudentFeedbackSurveyView.as_view(), name="student-feedback-survey"),
	path('transcript-generator/', views.TranscriptView.as_view(), name="transcript-generator"),
	path('white-out/', views.WhiteOutView.as_view(), name="white-out"),
	path('stochastic-optimization/', views.StochasticOpView.as_view(), name="stochastic-optimization"),
	path('degree-audimatons/', views.DegreeAudimatonsView.as_view(), name="degree-audimatons"),
	path('dream-setup/', views.MySetUpView.as_view(), name="dream-setup"),
	path('soccer-tourny/', views.TournyView.as_view(), name="soccer-tourny"),
	path('zeta/', views.ZetaView.as_view(), name="zeta"),
	path('curvature/', views.CurvatureView.as_view(), name="curvature"),
	path('gradient-descent/', views.GradientDescentView.as_view(), name="gradient-descent"),
	path('logistic-curve/', views.LogisticCurveView.as_view(), name="logistic-curve"),
	path('sparkML-higgs/', views.SparkHiggsView.as_view(), name="sparkML-higgs"),
	path('website-feedback-survey/', views.WebsiteFeedbackSurveyView.as_view(), name="website-feedback-survey"),

	]