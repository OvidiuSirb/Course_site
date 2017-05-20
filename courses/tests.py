from django.test import TestCase
from .models import Course,Step
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = "Python Regex",
            description = "Learn to write regex",
        )
        now = timezone.now()
        #self.assertLess(course.created_at,now)


class CourseViewsTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title = "Python Regex",
            description = "Learn to write regex",
        )
        self.course2 = Course.objects.create(
            title = "Python Testing",
            description = "Learn to write tests",
        )
        self.step = Step.objects.create(
            title="Introduction to regex",
            description="Learn to write regexfsa.fs,af.a.fas.a",
            course = self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse("courses:list"))
        self.assertEqual(resp.status_code,200)
        self.assertIn(self.course,resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])

        self.assertTemplateUsed(resp,'courses/course_list.html')
        self.assertContains(resp,self.course.title)

    def test_course_detail(self):
        resp = self.client.get(reverse('courses:detail',
                                       kwargs={'pk':self.course.pk}))
        self.assertEqual(resp.status_code,200)
        self.assertEqual(self.course,resp.context['course'])

    def test_step_detail(self):
        resp = self.client.get(reverse('courses:step',
                               kwargs={'course_pk':self.course.pk,
                                       'step_pk':self.step.pk
                               }))
        self.assertEqual(resp.status_code,200)
        self.assertEqual(self.step,resp.context['step'])