#version 330

#define PI (3.1415926)
#define FRAME_RATE (60)
#define HEIGHT (512)
#define WIDTH (512)

out vec3 f_color;

uniform int u_time;

const float freq = 0.5;

const vec3 my_color = vec3(1.0, 0.0, 1.0);

void main() {
    //f_color = my_color * (1.0 + cos(2 * PI * u_time / FRAME_RATE * freq)) * 0.5;
    vec2 uv = vec2(gl_FragCoord.x / WIDTH, gl_FragCoord.y / HEIGHT) * 2.0 - 1.0;

    float r = (uv.x + 1.0) * 0.5;
    float g = (1.0 - uv.x) * 0.5;
    float b = min(1.0 - abs(uv.y)*2.0, 1.0);

    f_color = vec3(r,g,b);
}