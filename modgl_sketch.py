import moderngl_window as glw
import moderngl as gl
from helpers import read_file
import numpy as np
import time

VERTEX_SHADER_PATH = "shaders/vertex_shader.glslv"
FRAGMENT_SHADER_PATH = "shaders/fragment_shader.glslf"


def main():
    window_cls = glw.get_local_window_cls("pyglet")
    window = window_cls(
        size=(512, 512),
        fullscreen=False,
        title="ModernGL Window",
        resizable=False,
        vsync=True,
        gl_version=(3, 3),
    )

    ctx = window.ctx
    glw.activate_context(window, ctx=ctx)
    window.clear()
    window.swap_buffers()

    prog = ctx.program(
        vertex_shader=read_file(VERTEX_SHADER_PATH),
        fragment_shader=read_file(FRAGMENT_SHADER_PATH),
    )

    x = np.linspace(-1.0, 1.0, 50)
    y = np.random.rand(50) - 0.5

    vertices = np.dstack([x, y])

    vbo = ctx.buffer(vertices.astype("f4").tobytes())
    vao = ctx.vertex_array(prog, vbo, "in_vert")

    fbo = ctx.framebuffer(color_attachments=[ctx.texture((512, 512), 3)])

    uniform_time = prog["u_time"]
    time_inc = 0

    t_prev = time.time()

    while not window.is_closing:
        uniform_time.value = time_inc

        fbo.use()
        fbo.clear(0.0, 0.0, 0.0, 1.0)
        vao.render(gl.LINE_STRIP)

        ctx.copy_framebuffer(window.fbo, fbo)

        window.swap_buffers()

        time_inc += 1

        t_now = time.time()
        dt = t_now - t_prev
        t_prev = t_now
        if time_inc % 30 == 0:
            print(f"fps: {1/dt:.1f}", end="\r")


main()
