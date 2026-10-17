import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

P=Path(__file__).resolve().parents[1]/'skills/figcraft-scenario-playbooks/scripts/run_recipe.py'
s=importlib.util.spec_from_file_location('fig_recipe',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)


class Bindings(unittest.TestCase):
    def test_returned_id_keeps_native_type(self):
        self.assertEqual(m.resolve({'parent':{'$ref':'root.id'}},{'root':{'id':842}}),{'parent':842})
    def test_unresolved_binding_fails_before_native_write(self):
        with tempfile.TemporaryDirectory() as d:
            calls=[]
            with self.assertRaisesRegex(ValueError,'Unresolved'):
                m.execute_recipe({'steps':[{'command':'node.create','params':{'parent':{'$ref':'missing.id'}}}]},lambda *a:calls.append(a),d,Path(d)/'out.figcraft')
            self.assertEqual(calls,[])
    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'old.figcraft';p.write_bytes(b'user')
            with self.assertRaisesRegex(ValueError,'already exists'):m.execute_recipe({'steps':[]},lambda *a:None,d,p)
            self.assertEqual(p.read_bytes(),b'user')
    def test_native_capture_and_following_parent(self):
        with tempfile.TemporaryDirectory() as d:
            batches=[]
            def run(*args):
                steps=json.loads(Path(args[1]).read_text());batches.append(steps);Path(args[-1]).write_bytes(b'saved')
                return '\n'.join(json.dumps({'step':i,'ok':True,'result':{'id':842+i}}) for i,_ in enumerate(steps))
            recipe={'steps':[{'command':'node.create','params':{},'capture':'root'},{'command':'node.create','params':{'parent':{'$ref':'root.id'}}}]}
            out=Path(d)/'out.figcraft';m.execute_recipe(recipe,run,d,out)
            self.assertEqual(batches[1][0]['params']['parent'],842);self.assertEqual(out.read_bytes(),b'saved')
    def test_existing_input_skips_file_new(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'in.figcraft';p.write_bytes(b'user');calls=[]
            def run(*args):
                commands=json.loads(Path(args[1]).read_text());calls.extend(x['command'] for x in commands);Path(args[-1]).write_bytes(b'new');return json.dumps({'ok':True,'result':{'id':9}})
            m.execute_recipe({'steps':[{'command':'file.new','params':{},'newDocumentOnly':True},{'command':'node.create','params':{},'capture':'root'}]},run,d,Path(d)/'out.figcraft',p)
            self.assertEqual(calls,['node.create']);self.assertEqual(p.read_bytes(),b'user')


if __name__=='__main__':unittest.main()
