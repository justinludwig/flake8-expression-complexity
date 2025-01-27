import ast
import itertools
from typing import Iterable, Callable, Tuple, List


def iterate_over_expressions(node: ast.AST) -> Iterable[ast.AST]:
    additionals_subnodes_info: List[Tuple[Tuple, Callable]] = [
        ((ast.If, ast.While), lambda n: n.test),
        ((ast.For, ), lambda n: n.iter),
    ]
    nodes_with_subnodes = (
        ast.FunctionDef, ast.AsyncFunctionDef,
        ast.If, ast.For, ast.Module,
        ast.ClassDef, ast.Try, ast.With, ast.While,
    )
    for bases, subnodes_getter in additionals_subnodes_info:
        if isinstance(node, bases):
            yield subnodes_getter(node)
    nodes_to_iter = (
        _get_try_node_children(node)
        if isinstance(node, ast.Try)
        else getattr(node, 'body', [])
    )
    for child_node in nodes_to_iter:
        if isinstance(child_node, nodes_with_subnodes):
            for subnode in iterate_over_expressions(child_node):
                yield subnode
        else:
            yield child_node


def _get_try_node_children(try_node: ast.Try):
    return itertools.chain(try_node.body, try_node.finalbody, *[n.body for n in try_node.handlers])
