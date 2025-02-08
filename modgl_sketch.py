from helpers import *
import moderngl, glfw, time
import numpy as np


WINDOW_SIZE = 1280, 720


def main():
    if not glfw.init():
        raise Exception("GLFW can't be initialised.")

    # Create windowed-mode window and its OpenGL context
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(*WINDOW_SIZE, "GLFW Window", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created.")

    glfw.make_context_current(window)
    ctx = moderngl.get_context()

    program = ctx.program(read_file("shader.vert"), read_file("shader.frag"))

    vertices = (
        np.dstack([x := np.linspace(-1.0, 1.0, 5_000), np.sin(2 * np.pi * x) * 0.5])
        .astype("f4")
        .tobytes()
    )

    vao = ctx.vertex_array(program, ctx.buffer(vertices), "in_vert")

    time_inc = 0
    t_prev = time.time()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        ctx.clear(0.0, 0.0, 0.0, 1.0)

        # Update shader uniforms
        vao.program["u_time"] = time_inc

        # Render vertices
        vao.render(moderngl.LINE_STRIP)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        time_inc += 1

        t_now = time.time()
        dt = t_now - t_prev
        t_prev = t_now
        if time_inc % 30 == 0:
            print(f"fps: {1/dt:.1f}", end="\r")


main()
