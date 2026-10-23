"""Interactive vector drawing lab reconstructed from previously discussed practice.

Install dependency: python -m pip install pygame
Run from repository root: python pygame-labs/vector_lab.py

This is a learning example, not a claim that the original classroom file was
recovered byte-for-byte. It demonstrates Vector2 arithmetic and screen mapping.
"""

import pygame


WIDTH, HEIGHT = 800, 600
BACKGROUND = (24, 28, 38)
WHITE = (235, 239, 245)
COLORS = {
    "A": (80, 190, 255),
    "B": (255, 180, 80),
    "A + B": (110, 230, 160),
    "A - B": (230, 120, 180),
    "1.5A": (190, 150, 255),
}
ORIGIN = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
SCALE = 2.0


def to_screen(vector: pygame.Vector2) -> tuple[int, int]:
    """Convert Cartesian coordinates to screen coordinates (y points up)."""
    return round(ORIGIN.x + vector.x * SCALE), round(ORIGIN.y - vector.y * SCALE)


def draw_vector(surface: pygame.Surface, vector: pygame.Vector2, color: tuple, label: str) -> None:
    start = (round(ORIGIN.x), round(ORIGIN.y))
    end = to_screen(vector)
    pygame.draw.line(surface, color, start, end, 3)
    pygame.draw.circle(surface, color, end, 5)
    font = pygame.font.Font(None, 24)
    surface.blit(font.render(f"{label} = ({vector.x:g}, {vector.y:g})", True, color),
                 (end[0] + 8, end[1] - 18))


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Learning Journey — Vector Lab")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    a = pygame.Vector2(100, -50)
    b = pygame.Vector2(50, -100)
    vectors = [
        ("A", a),
        ("B", b),
        ("A + B", a + b),
        ("A - B", a - b),
        ("1.5A", 1.5 * a),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND)
        pygame.draw.line(screen, (100, 108, 125), (0, ORIGIN.y), (WIDTH, ORIGIN.y), 1)
        pygame.draw.line(screen, (100, 108, 125), (ORIGIN.x, 0), (ORIGIN.x, HEIGHT), 1)
        pygame.draw.circle(screen, WHITE, (round(ORIGIN.x), round(ORIGIN.y)), 4)

        for label, vector in vectors:
            draw_vector(screen, vector, COLORS[label], label)

        heading = font.render("Vector arithmetic: A, B, A+B, A-B, 1.5A", True, WHITE)
        screen.blit(heading, (18, 16))
        footer = pygame.font.Font(None, 22).render("Close the window to exit", True, WHITE)
        screen.blit(footer, (18, HEIGHT - 28))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
