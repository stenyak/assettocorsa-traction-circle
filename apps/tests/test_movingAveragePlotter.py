from unittest import TestCase

from moving_average_plotter import MovingAveragePlotter


class TestMovingAveragePlotter(TestCase):
    def test_plotMovingAverage(self):
        points = []
        for x in range(1, 10):
            points.append({"x": x, "y": x, "z": x})

        moving_average_plotter = MovingAveragePlotter()

        averagedPoints = moving_average_plotter.plotMovingAverage(points)

        self.assertEqual(5, len(averagedPoints))
        self.assertEqual(3, averagedPoints[0]['x'])  # 1,2,3,4,5 = average of 3
        self.assertEqual(3, averagedPoints[0]['y'])  # 1,2,3,4,5 = average of 3
        self.assertEqual(3, averagedPoints[0]['z'])  # 1,2,3,4,5 = average of 3
        self.assertEqual(4, averagedPoints[1]['x'], str(averagedPoints))  # 2,3,4,5,6 = average of 4
        self.assertEqual(4, averagedPoints[1]['y'], str(averagedPoints))  # 2,3,4,5,6 = average of 4
        self.assertEqual(4, averagedPoints[1]['z'], str(averagedPoints))  # 2,3,4,5,6 = average of 4

    def test_shouldNotPlotMuchIfTheresNotEnoughDataPoints(self):

        points = []
        moving_average_plotter = MovingAveragePlotter()

        averagedPoints = moving_average_plotter.plotMovingAverage(points)
        self.assertEqual(0, len(points))

