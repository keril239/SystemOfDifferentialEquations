from manim import *

class TestSystemOfDifferentialEquations(ThreeDScene):
    def construct(self):
        # Добавляем оси
        axes = ThreeDAxes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            z_range=[-6, 6],
            x_length=10,
            y_length=10,
            z_length=6
        )
        self.add(axes)

        # Устанавливаем ориентацию камеры
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Начинаем вращение камеры
        self.begin_ambient_camera_rotation(rate=0.1)

        # Начальные условия для системы дифференциальных уравнений
        x, y, z = 1, 1, 0
        dt = 0.001
        num_steps = 10000

        # Массив для хранения точек траектории
        trajectory_points = []

        # Численное интегрирование системы дифференциальных уравнений
        for _ in range(num_steps):
            dx = (-y + x * (1 - z * z - x * x - y * y)) * dt
            dy = (x + y * (1 - z * z - x * x - y * y)) * dt

            x += dx
            y += dy

            trajectory_points.append([x * 2, y * 2, z * 2])

        # Создаем траекторию как параметрическую функцию
        trajectory_curve = ParametricFunction(
            lambda t: trajectory_points[int(t * (num_steps - 1))],
            t_range=[0, 1],
            color=RED
        )

        # Анимация для создания траектории
        self.play(Create(trajectory_curve), run_time=10, rate_func=linear)

        '''
        # Создаем точку, которая будет двигаться по траектории
        moving_dot = Dot3D(point=trajectory_points[0], radius=0.1, color=YELLOW)
        self.add(moving_dot)

        # Анимация точки вдоль траектории
        self.play(MoveAlongPath(moving_dot, trajectory_curve), run_time=5, rate_func=linear)
        '''

class SystemOfDifferentialEquations(ThreeDScene):
    def construct(self):
        # Добавляем оси
        axes = ThreeDAxes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            z_range=[-6, 6],
            x_length=10,
            y_length=10,
            z_length=6
        )
        self.add(axes)

        # Устанавливаем ориентацию камеры
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Начинаем вращение камеры
        self.begin_ambient_camera_rotation(rate=0.1)

        # Начальные условия для системы дифференциальных уравнений
        dt = 0.001
        num_steps = 10000
        
        # Функция для численного интегрирования системы дифференциальных уравнений
        def systemofdifferentialequations_trajectory(x_start, y_start, z_start):
            x, y, z = x_start, y_start, z_start
            trajectory_points = []

            for _ in range(num_steps):
                dx = (-y + x * (1 - z * z - x * x - y * y)) * dt
                dy = (x + y * (1 - z * z - x * x - y * y)) * dt

                x += dx
                y += dy

                trajectory_points.append([x * 2, y * 2, z * 2])
            return trajectory_points

        # Список начальных условий для нескольких траекторий
        initial_conditions = [
            (-1, -1, -1.25),
            (-1, -1, -1),
            (-1, -1, -0.75),
            (-1, -1, -0.5),
            (-1, -1, -0.25),
            (1, 1, 0),
            (1, 1, 0.25),
            (1, 1, 0.5),
            (1, 1, 0.75),
            (1, 1, 1),
            (1, 1, 1.25)
        ]

        # Список цветов для разных траекторий
        colors = [RED, BLUE, GREEN, YELLOW]

        # Список для хранения всех траекторий
        trajectories = []

        for i, (x0, y0, z0) in enumerate(initial_conditions):
            trajectory_points = systemofdifferentialequations_trajectory(x0, y0, z0)

            # Создаем траекторию как параметрическую функцию
            trajectory_curve = ParametricFunction(
                lambda t, trajectory_points=trajectory_points: trajectory_points[int(t * (num_steps - 1))],
                t_range=[0, 1],
                color=colors[i % 4]
            )

            trajectories.append(trajectory_curve)

        # Анимация для создания всех траекторий
        self.play(*[Create(trajectory) for trajectory in trajectories], run_time=10, rate_func=linear)